import sys
import io
import re

f = open(sys.argv[1], 'r')
o = open('foo', 'w')

section = re.compile('^[0-9]+$')
timestamp = re.compile('^[0-9:,]+\\s-->\\s[0-9:,]+$')
whitespace = re.compile('\\s+')

for line in iter(f.readline, ''):
    if not section.match(line) and \
            not timestamp.match(line) and \
            not whitespace.match(line):
                o.write(line)

f.close()
o.close()

