#Chapter 10 - Sample 10-2


txt = 'but what soft light in yonder window breaks'
words = txt.split()
t = list()

for word in words: 
    t.append((len(word), word))
    
print 'list-t before sort', t
t.sort(reverse = True)
print 'list-t after sort', t

res = list()

for length, word in t:
    res.append(word)
    
print res