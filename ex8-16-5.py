#Chapter 8 - Exercise 8-16-5

in_file = open('mbox-short.txt')

for line in in_file:
    if line.startswith('From'):
        value = line.split(':')[1]
        value.lstrip().rstrip()
        print value