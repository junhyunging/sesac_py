# 파이썬은 변수라는걸 지정하는 키워드가 없음.. let var const

x=5
y=3

print(x+y)

print(x % y) #나머지값
print(x ** y)

str_x = "100"

# print(x+str_x) 문자와 숫자는 더할수없음

int_x = int(str_x) #문자를 숫자(정수=integer)로 변환
print("문자열 x :", str_x)
print("숫자열 x :", int_x)

print (x+int_x)

#비트 연산잔
print ("비트연산자")
print(1 & 1)
print(1 & 0)
print(0 & 1)
print(0 & 0)
print("비트연산자 or")
print(1 | 1)
print(1 | 0)
print(0 | 1)
print(0 | 0)

#주의사항 (기계는 항상 2진수를 사용함..)
print(x & y) # 5 & 3 1: 101 & 011 = 1
print(x | y) # 101 | 011 = 111 7
