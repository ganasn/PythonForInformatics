#Chapter 8 - Exercise 8-16-6

numbers = list()
while True:
    value = raw_input('Enter integer or done>')
    if value == 'done' and len(numbers) > 0:
        print 'Average of %d numbers keyed until now is %d with a maximum of %d and minimum of %d' % (len(numbers), sum(numbers)/len(numbers), max(numbers), min(numbers))
        break
    elif value == 'done' and len(numbers) == 0:
        print 'no average to compute'
        break
    else:    
        try:
            numbers.append(int(value))
        except:
            print 'Value entered is NOT an integer'
            continue
