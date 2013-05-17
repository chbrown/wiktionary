meta_languages_text = open('Meta_Languages.tsv')

# ab  Abkhaz  "Abkhaz, Abkhazian, Abxazo"
iso2name = dict()
name2iso = dict()
for line_bytes in meta_languages_text:
    line = line_bytes.decode('utf8')
    iso, primary_name, names = [part.strip().strip('"') for part in line.split(u'\t')]

    for name in names.split(','):
        name = name.strip()
        if name in name2iso:
            print '%s is in name2iso twice! Meta-ambiguity!' % name
        name2iso[name] = iso
    iso2name[iso] = primary_name


def dict_lit(d):
    return '{\n%s}' % ''.join('    u"%s": u"%s",\n' % keyval for keyval in sorted(d.items()))

print 'iso2name = %s' % dict_lit(iso2name)
print 'name2iso = %s' % dict_lit(name2iso)
