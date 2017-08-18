#Chapter 11 - Section 11-3

import re
file_handler = open('mbox-short.txt')
for line in file_handler:
    if re.findall('^X.*Conf', line): 
        print 'full string is %s' % re.findall('^X\S*Confidence: [0-9.]+', line)
        print 'just the number is %s' % re.findall('^X\S*Confidence: ([0-9.]+)', line)