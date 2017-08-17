#Chapter 10 - Exercise 10-11-3

file_text = open('mbox-short.txt').read()
freq = dict()

for char in file_text:
    if char.isalpha():
        if char.lower() not in freq:
            freq[char.lower()] = 1
        else:
            freq[char.lower()] += 1
            
print freq
            
sort = list()
for key, value in freq.items():
    sort.append((key, value))
    sort.sort()

print sort, len(sort)

#Making the sort list() into another dict() for kicks!
sort_freq = dict()
count = 0
while count < len(sort):
    print sort[count][0], sort[count][1]
    sort_freq[sort[count][0]] = sort[count][1]
    count += 1

#note that sort_freq dict() is still NOT sorted like sort list() is!!!
print sort_freq


#
#txt = 'but what soft light in yonder window breaks'
#words = txt.split()
#t = list()
#
#for word in words: 
#    t.append((len(word), word))
#    
#print 'list-t before sort', t
#t.sort(reverse = True)
#print 'list-t after sort', t
#
#res = list()
#
#for length, word in t:
#    res.append(word)
#    
#print res