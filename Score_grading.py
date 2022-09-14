score = input("Please input a score between and including 0.0 and 1.0: ")
error = "Bad score!"

try:
    score = float(score)
    if score >= 0.0 and score <= 1.0:
        if score >= 0.9:
            grade = 'A'
        elif score >= 0.8:
            grade = 'B'
        elif score >= 0.7:
            grade = 'C'
        elif score >= 0.6:
            grade = 'D'
        elif score < 0.6:
            grade = 'F'
    else:
        print(error)
        
    print(grade)
    
except:
    print(error)