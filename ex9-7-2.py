#Chapter 9 - Exercise 9-7-2

#Following statement converts file_text into a string (of characters) on which lines applies at character level instead of line level
#file_text = open('mbox-short.txt').read()
#Following statement rectifies it by keeping file_text as a file handler and not a string

file_text= open('mbox-short.txt')

#print file_text

freq = dict()
freq = {
    'Sun':0,
    'Mon':0,
    'Tue':0,
    'Wed':0,
    'Thu':0,
    'Fri':0,
    'Sat':0
}

for lines in file_text:
    if lines.startswith('From'):
#        print lines
        for days in lines.split():
            if days in freq:
                freq[days] += 1

print freq