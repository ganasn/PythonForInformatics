#Chapter 8 - Lists 

#Attempting to compute arithmetic mean usings lists



while True:
    option = raw_input('average or quit?>')
    if option == 'quit':
        print 'Exiting program'
        break
    elif option == 'average':
        numbers = list()
        while True:
            value = raw_input('Enter integer or done>')
            if value == 'done' and len(numbers) > 0:
                print 'Average of %d numbers keyed until now is %d' % (len(numbers), sum(numbers)/len(numbers))
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
    else:
        print 'Did not recognize input'
        continue