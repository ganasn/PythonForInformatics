#Chapter 11 - Exercise 11-9-1

import re

file_handler = open('mbox-short.txt')
while True:
    #        Need to reset file_handler to beginning of file
    file_handler.seek(0)
    reg_ex = raw_input('Enter RegEx to search or \'done\' to quit>')
    line_count = 0
    if reg_ex == 'done':
        break
    else:
#        print 'within else'
        for line in file_handler: 
#            print 'within for', line_count
            if re.findall(reg_ex, line):
                line_count += 1
        print 'RegEx %s appeared in file %d times' %(reg_ex, line_count)