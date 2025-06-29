for i in range(5):
    print(i)

for i in range(1,10): # 끝값은 포함하지 않는다.
    print(i)    
    
for i in range(1,10,2): # 1부터 10까지 2씩 건너뛴다
    print(i)
    
for i in range(1,10,3): # 1부터 10까지 3씩 건너뛴다
    print(i)
    
fruits = ['apple', 'banana', 'cherry']
for f in fruits:
    print(f)

for i, f in enumerate(fruits):
    print(i, f)    
    
str = "Hello World"
for char in str:
    print(char)
    
# 위 문장에서 o의 갯수를 구하시오
count_o = 0
for char in str:
    if char == 'o':
        count_o += 1
        print(f'{str} 문장내의 o갯수는 {count_o}개 입니다.')
        
        
