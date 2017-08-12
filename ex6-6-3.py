#Exercise 6-6-3

#from sys import *

def count(string, letter):
    count = 0 
    char = ''
    for char in string.lower():
#        if char == letter:
        if char == letter.lower():
            count += 1
    return count


string = raw_input('Enter string>')
letter = raw_input('Enter letter to count>')
print 'Letter \'%c\' appears in string \'%s\' %d times' %(letter, string, count(string, letter))