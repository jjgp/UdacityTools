import sys
import io
import re
from docx import Document

def add_transcript_to_document(path, doc):
    f = open(path, 'r')
    o = io.StringIO()

    section = re.compile('^[0-9]+$')
    timestamp = re.compile('^[0-9:,]+\\s-->\\s[0-9:,]+$')
    whitespace = re.compile('\\s+')
    for line in iter(f.readline, ''):
        if not section.match(line) and \
                not timestamp.match(line) and \
                not whitespace.match(line):
                    line = line.strip()
                    line += ' '
                    o.write(line.decode('utf-8'))

    f.close()
    doc.add_paragraph(o.getvalue())
    o.close()

d = Document()
add_transcript_to_document(sys.argv[1], d)
d.save('foo.docx')

