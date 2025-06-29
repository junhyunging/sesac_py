score = 80

def getGrade(score):
    if score>90:
        grade = ("A학점")
    elif score >=80:
        grade = ("B학점")
    elif score >= 80:
        grade = ("C학점")
    else:
        grade = ("F학점")
        
        return grade
    
    john = getGrade(70)
    print("존의 학점 : ", john)
    
    jane = getGrade(95)
    print("존의 학점 : ", jane)
    
    #사용자에게 입력받기
    user = input("점수를 입력하시오: ")
    
    # 내장함수 (built-in functions)
    userScore = getGrade(int(user))
    print(userScore)