str = "Hello World"
str2 = "Welcome to sesac class"
print(str)

#라이브러리 함수들로 만들어 놨음..
print(str.lower()) #글자를 다 소문자로 바꿈
print(str.upper()) #대문자로
print(str.capitalize()) #문장의 시작을 대문자로
print(str2.title()) #문장의 단어 단어마다 대문자로..
print(str2.strip()) #앞뒤 불필요한 공백 제거
print(str2.lstrip()) #왼쪽 공백 지우기 
print(str2.rstrip()) #오른쪽 공백 지우기
print(str.split()) #문장을 단어 단위로 짜른다
print(str2.split()) #문장을 단어 단위로 짜른다

words = str2.split()
print(words[0].upper()) #[0] 0번쨰 인덱스 가져오기
print(",".join(words))
print(" ".join(words))
print("-".join(words))

print(str.startswith("Hello")) #~~으로 시작하는지
print(str.startswith("hello"))

