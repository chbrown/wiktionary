import sys

# Code    Name    Alternative Code    Alternative Names
iso2name = dict()
name2iso = dict()
for line_bytes in open('Index_to_templates.tsv'):
    line = line_bytes.decode('utf8')
    primary_iso, primary_name, isos, names = [part.strip().strip('"') for part in line.split(u'\t')]

    for name in [primary_name] + names.split(','):
        name = name.strip()
        # if name in name2iso:
            # print '%s is in name2iso twice! Meta-ambiguity!' % name
        name2iso[name] = primary_iso

    for iso in [primary_iso] + isos.split(','):
        iso2name[iso] = primary_name

name2iso.pop('', None)
iso2name.pop('', None)


def dict_lit(d):
    return '{\n%s}' % ''.join('    u"%s": u"%s",\n' % keyval for keyval in sorted(d.items()))


def stdout(s):
    bytes = s.encode('utf8')
    sys.stdout.write(bytes)
    sys.stdout.flush()

stdout('# -*- coding: utf-8 -*-\n')
stdout('iso2name = %s\n' % dict_lit(iso2name))
stdout('name2iso = %s\n' % dict_lit(name2iso))
