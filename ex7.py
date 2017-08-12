#Chapter 7 - File Operations

in_file = open('mbox-short.txt')
out_file = open('mbox-copy.txt', 'a')

#text = fout.readline()
#print 'text is %r' % text
#for lines in text:
#    print lines

#count = 0
for line in in_file:
#    if count < 20: 
#        count += 1 
#        print line
    line = line.rstrip()
    if not line.startswith('From'):
        out_file.write(line + '\n')

out_file.close()        
        
        
        
