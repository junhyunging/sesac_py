#딕셔너리라고 부름..
#key:value 로 구분됨..
my_dict = {"name":"Alice", "age":25 , "location":"Seoul"}
print(my_dict)

print(my_dict["name"]) # 'name' 이라는 키가 가지고 있는 값은?
print(my_dict["age"])

user1 = {"name":"Bob", "age":30, "location": "Busan"}
print(user1["name"])
print(user1["age"])
print(user1["location"])

user1["age"] = 31
print(user1["age"])
print(user1)

user1["car"] = "k5"
print(user1)

user1["car"] = ""
print(user1)

# 특정 키값을 지우는 키워드가 del 키워드임
del user1["car"]
print(user1)

print(user1.keys()) #모든 키
print(user1.values()) #모든 값
print(user1.items()) # 키-값 쌍으로 출력

user_items = user1.items()
print(list(user_items)) 

# 리스트와,튜플과, 딕셔너리를 구분할줄 알고, 자유롭게 다룰줄 알면 됨..
#[],(),{}

