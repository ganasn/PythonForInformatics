#Exercise 6-14-5

str = 'Confidence: 0.8457'
if len(str) > 0:
    index = str.find(':')
    print index
    value = str[index+1:]
    print 'Confidence is %f' % float(value)