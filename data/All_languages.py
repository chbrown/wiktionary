import re

header_re = re.compile(r'''=== \[\[([^\]]+?)\]\] ===
\| (\w+)''')

all_languages_text = open('All_languages.txt').read().decode('utf8')

matches = sorted(header_re.findall(all_languages_text), key=lambda pair: pair[1])
for name, code in matches:
    print "    '%s': u'%s'," % (code, name)
