#Chapter 9 - Exercise 9-7-5

file_text= open('mbox-short.txt')

#print file_text

freq = dict()

for lines in file_text:
    if lines.startswith('From'):
#        I'm concerned that this list designation may not scale
        email = (lines.split()[1]).split('@')[1]
        if email in freq:
            freq[email] += 1
        else:
            freq[email] = 1

print freq