#Chapter 10 - Exercise 10-11-2

#From zqian@umich.edu Fri Jan  4 16:10:39 2008
#From: stephen.marquard@uct.ac.za


file_text= open('mbox-short.txt')

freq = dict()

for lines in file_text:
#    Get only those lines that have an email address
    if lines.startswith('From'):
        new_line = lines.split()
#        Split to separate just email addresses from email address w/ date-time stamp
        if len(new_line) > 2:
            hour_freq = new_line[len(new_line)-2].split(':')[0]
            print hour_freq
            if hour_freq not in freq:
                freq[hour_freq] = 1
            else:
                freq[hour_freq] += 1
        
print freq