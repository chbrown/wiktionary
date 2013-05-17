# -*- coding: utf-8 -*-
from lxml import etree
import argparse
import os
import re
import sys
from reader import chunker
import languages

langs = re.compile('\{\{etyl.+?(?:lang=)?(\w+)\}\}', re.I)


def consolidate_iso(iso):
    return languages.name2iso[languages.iso2name[iso]]


def parse_page(page):
    '''
    Returns a pair (word, source_languages)
    e.g.,
        ('Burgundy', ['fr', 'hy', 'la', 'la', 'la'])
    or,
        ('Burunika', [])
    '''
    tree = etree.fromstring(page)
    word = tree.xpath('/page/title')[0].text

    # if not word.startswith('Wiktionary:'):
    codes = []
    body = tree.xpath('/page/revision/text')[0].text
    if body:
        codes = langs.findall(body)

    return word, codes


parser = argparse.ArgumentParser(description='Wiktionary parser')
parser.add_argument('--take', type=int)
opts = parser.parse_args()

corpora_path = os.environ['CORPORA']
wiktionary_xml = corpora_path + '/wiktionary/enwiktionary-20130503-pages-articles-multistream.xml'

with open(wiktionary_xml) as wiktionary_fp:
    counter = 0
    for page in chunker(wiktionary_fp, '  <page>\n', '  </page>\n'):
        word, page_isos = parse_page(page)

        # if not word.startswith('Wiktionary:'):
        if len(page_isos) > 0:
            # languages.iso2name will not contain iso mostly in weird, typo-ish cases
            page_isos = [consolidate_iso(iso) for iso in page_isos if iso in languages.iso2name]
            # page_languages = sorted(list(set(page_languages)))
            line = '%s\t%s\n' % (word, ','.join(page_isos))
            sys.stdout.write(line.encode('utf8'))
            sys.stdout.flush()
            counter += 1

            if counter % 100 == 0:
                sys.stderr.write('\r%7d' % counter)
                sys.stderr.flush()

            if opts.take and counter > opts.take:
                break
