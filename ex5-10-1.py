#Exercise 5-10-1

#Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

#total, count, & average

count = 0
total = 0.0
average = 0.0

while True:
    try:
        value = raw_input('Enter value>')
        if value == 'done':
            break
        else:
#        elif type(value) == 'int':
            total += int(value)        
            count += 1
            average = total/count
#        else:
    except: 
        print 'bad data'
        continue

print 'Count is %d, average is %f, & total is %d' %(count, average, total)