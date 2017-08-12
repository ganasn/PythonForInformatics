#Exercise 6-14-5

str = 'Let\'s look at the probabilty at: 0.8457'
if len(str) > 0:
    index = str.find(':')
    print index
    index += 1
    while True:
        if str[index].isdigit(): 
            value = str[index:]
            break
        else:
            index += 1
            continue
            
    print 'Confidence is %f' % float(value)