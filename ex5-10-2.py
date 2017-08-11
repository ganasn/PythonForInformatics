#Exercise 5-10-2

#Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

#max & min

maximum = None
minimum = None

while True:
    try:
        value = raw_input('Enter value>')
        if value == 'done':
            break
        else:
            if int(value) > maximum:
                maximum = int(value)
            if minimum < int(value):
                minimum = int(value)
    except: 
        print 'bad data'
        continue

if maximum != None and minimum != None:
        print 'Maximum is %d & minimum is %d' %(maximum, minimum)
else:
    print 'No maximum & minimum'