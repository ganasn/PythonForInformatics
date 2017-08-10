#Branching from Chapter 3 - 3.11 - Ex 3
#For Chapter 4 - Ex 7

#score = 0
#grade = ''

def compute_grade(score):
    if score < 0.0 or score > 1.0:
        print 'bad score'
        exit(0)
    else:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7: 
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
            
    return grade
        
score = float(raw_input('Enter score between 0.0 & 1.0>'))
grade = compute_grade(score)
print 'Score is %f and corresponding grade is %s' % (score, grade)