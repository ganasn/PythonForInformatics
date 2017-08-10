#3.11 - 1

hours = 0
rate = 0
pay = 0

try:
    hours =int(raw_input('Enter hours>'))
    rate = int(raw_input('Enter rate>'))
    if rate < 0 or hours < 0:
        print 'Inputs can NOT be negative'
        exit(0) 
    if hours > 0 and hours < 41:
#        print 'In if'
        pay = hours * rate
    elif hours > 40:
#        print 'In elif'
        pay = (hours - 40) * rate * 1.5 + 40 * rate
    else:
        print 'Inputs are incorrect'
    print 'Pay is %d' % pay
except:
    print 'Inputs are incorrect, please restart'