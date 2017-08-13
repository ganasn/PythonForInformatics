#Exercise - 8-16-4

all_words = list(open('romeo.txt').read().upper().split())
all_words.sort()
print all_words

unique_words = list()

#Given that first word going into new list is going to be unique anyway...
unique_words.append(all_words[0])
#print all_words[0]
#print unique_words

for words in all_words:
#    print words
    if unique_words[len(unique_words)-1] == words:
        continue
    else:
        unique_words.append(words)

print 'All words is ', all_words, ' and its length is ', len(all_words)
print 'Unique words is ', unique_words, ' and its length is ', len(unique_words)