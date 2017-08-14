#Chapter 9 - Exercise 9-1

file_text = open('mbox-copy.txt').read().split()

counter = 0
file_hash = dict()
for words in file_text:
    counter += 1
    file_hash[counter] = words
#print file_hash
value = raw_input('Enter check word>')    
if value in file_hash.values(): 
    print 'Word in file'
else:
    print 'Word not in file'