#Chapter 11 - Trivial RegEx exercise - 11-0

import re
file_handler = open('mbox-short.txt')
for line in file_handler:
    if re.search('From:', line):
        print line