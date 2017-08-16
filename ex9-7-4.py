#Chapter 9 - Exercise 9-7-4

file_text= open('mbox-short.txt')

#print file_text

freq = dict()

for lines in file_text:
    if lines.startswith('From'):
#        I'm concerned that this list designation may not scale
        email = lines.split()[1]
        if email in freq:
            freq[email] += 1
        else:
            freq[email] = 1

print freq.items()

#email_list = freq.values()
#for keys in freq:
#    if max(email_list) == freq[keys]:
#        print freq[keys]
#        break
#    else:
#        continue

t = list()
#This just makes 't' a dict instead of a tuple
#t = freq

for keys in freq:
    t.append((keys, freq[keys]))
    
t.sort(reverse = True)
print t