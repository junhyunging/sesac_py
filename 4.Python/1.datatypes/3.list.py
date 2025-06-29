my_list = [1,2,3,4,5]
print(my_list)

print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[3])
# print(myList[5]) #이게 JS에서는 UNDIFIND, 그 외 다른언어(python)
print(my_list[4])
print(my_list[-1]) #거꾸로 갈 수 있음. 파이썬 특징. 대부분 허용 x

# 리스트 슬라이싱
print(my_list[1:3]) # 1번 인덱스부터 3번째를 포함하기전까지 [1] [2]
print(my_list[0:5]) # 0번 인덱스부터 5번째 전까지
print(my_list[0:2]) 
print(my_list[2:4])

print(my_list[:2]) # ㅅ시작부터 2를 포함하기 전까지 (0~! 까지)
print(my_list[2:]) # 인덱스 2부터 끝까지

# 리스트에 멤버 추가하기
print('-' * 50)
my_list.append(6) #기존에 리스트에 끝에 6추가
print(my_list)
my_list.insert(2,10) #인덱스 3번째 위치에 수자 10을 추가하겠음
print(my_list)

another_list =[7,8,9]
print(my_list)
print(another_list)
my_list.extend(another_list)
print(my_list)
print(another_list)

my_list.remove(10) #m나의 리스트에서 10이라는 숫자를 삭제할거야
print(my_list)

my_list.pop(3) #나의 리스트에서 인덱스 3에 있는 요소를 삭제할거야
print(my_list)

my_list.pop() # 인자를 안주면 마지막 요소 삭제
print(my_list)

my_list.clear() # 리스트 통쨰로 비우기
print(my_list)

print('-' * 50)
#리스트의 검색
my_list= [1,2,3,4,5,3,2,1]

index_of_3 = my_list.index(3) # 숫자 3의 인덱스는 어디인가요?
print(index_of_3)

count_2 = my_list.count(2) #2라는 숫자는 몇개가 있나요?
print(count_2)

print("--소팅전---")
print(my_list)
sorted_list = sorted(my_list) #이거는 인자를 받아서 반환하는 함수 (원본을 변경 하지 않음)
print(sorted_list)
print("--소팅후---")
print(my_list)

print('-' *50)
my_list.sort() #일부 함수는, 복제본을 만들어서 반환하는 애가 있고, 원본 데이터를 고치는 애가 있음
print(my_list) #뭐라고 정의 하지 않으면 ..오름차순(작은거 -> 큰거)

my_list.sort(reverse=True) # 내림차순 (큰거 -> 작은거)
print(my_list)

my_list.reverse() # 현재 리스트를 역순으로 전호나
print(my_list)

my_list2 = my_list.copy() #리스트 복제
print(my_list2)

# 리스트 컴프리헨션 # 파이썬의 매~~~~우 큰 특징(장점)
numbers = [x for x in range(10)] #리스트 안에 반복문 또는 조건문을 통해서, 리스트안에 채워질 요소를 정의할 수 있는 문법
print(numbers)
numbers = [mynumber for mynumber in range(5)]
print(numbers) 
numbers = [num for num in range(1,11)] #1부터 10까지 숫자를만들어서 이 리스트에 넣으십쇼
print(numbers) 
numbers = [num**2 for num in range(1,11)] #제곱수로 만들기
print(numbers)
numbers = [num             for num in range(1,11)          if num %2  == 0]
print(numbers)
