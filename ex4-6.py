#3.11 - 1 & 2
#Branching from Chapter 3 - 3.11 - Ex 2
#For Chapter 4 - Ex 6

#hours = 0
#rate = 0
#pay = 0


def compute_pay(hours, rate):
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
        exit(0)
    return pay
    



try:
    hours =int(raw_input('Enter hours>'))
    rate = int(raw_input('Enter rate>'))
    pay = compute_pay(hours, rate)
    print 'Pay is %d' % pay
except:
    print 'Inputs have to be positive integers, please restart'