numbers = [1,2,3,4,5,6,7,8,9,10]

# 여기를 순회하면서 짝수만 고르시오
for num in numbers:
    if(num %2 ==0):
        print(num)
    elif(num % 2 == 1):
        print(f'홀수는 : {num}')        
        
def getEvenNumbers(numbers):
    even_numbers = []
    for num in numbers:
     if num % 2 == 0:
         even_numbers.append(num)
         
         return even_numbers
     
even = getEvenNumbers(numbers)     
print(F'짝수는 : {even}')

# 다음 목록에서 성적이 A인 학생이 반환하시오
students = {
    '김철수' : 70,
    '김철숭' : 20,
    '김철민' : 70,
    '김철자' : 90,
    '김철강' : 20,
    '김철카' : 30,
    '김철차' : 40,
    '김철타' : 60,
    '김철파' : 93,
    '김철하' : 70,
}


def get_a_grade_student(students):
    result = []
    for name,score in students.items():
        if score >= 90:
            result.append(name)
        return result
    
a_students = get_a_grade_student(students)
print(a_students)
            