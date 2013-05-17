# -*- coding: utf-8 -*-
from lxml import etree
import argparse
import os
import re
import sys
from reader import chunker
import languages

langs = re.compile('\{\{etyl.+?(?:lang=)?(\w+)\}\}', re.I)


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
            page_languages = [languages.iso2name.get(iso, 'Missing: %s' % iso) for iso in sorted(page_isos)]
            line = '%s\t%s\n' % (word, ', '.join(page_languages))
            sys.stdout.write(line.encode('utf8'))
            counter += 1

            if counter % 100 == 0:
                sys.stdout.flush()

                sys.stderr.write('\r%7d' % counter)
                sys.stderr.flush()

            if opts.take and counter > opts.take:
                break


sys.stdout.flush()
sys.stderr.flush()
