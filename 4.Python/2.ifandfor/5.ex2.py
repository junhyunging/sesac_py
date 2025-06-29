users = [    
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "BMW"},
    {"name": "Bob", "age": 40, "location": "Busan", "car": "BMW"},
    {"name": "Charlie", "age": 35, "location": "Deagu", "car": "Audi"}
]


# 사용자 이름을 기반으로, 해당 사용자 정보를 가져오는 코드 구현하기
def find_uesr(name):
    for u in users:
        if u["name"] == name:
            return u
        
def find_users(name):
    result = []
    for u in users:
        if u["name"] == name:
            result.append(u)
    return result

def find_users_caseinsensitive(name):
    result = []
    for u in users:
        if u["name"].lower() == name.lower(): # DB내용도 사용자의 입력도 모두다 소문자로 바꾸기
            result.append(u)
    return result
        

print(find_users_caseinsensitive("BOB"))

def find_user2(name,age):
    for u in users:
        if u["name"] == name and u["age"] == age: #파이썬 연산자 우선순위가 있음
            return u
        
print(find_user2('Alice',25))

def find_uesr3(name=None,age=None):
    result = []
    
    for u in users:
        if name:
            if u["name"] == name:
                if age:
                    if u["age"] ==name:
                        
                     result.append(u)
                    
                else:
                    #이름은 매치되고 나이는 신경안 쓰는
                    result.append(u)     
        elif age:
            if u["age"] == age:
                result.append(u)
        else:
            result.append(u)
            
        return result    
    
    
    print("--간단한 재구현---")
    def find_uesr3(name=None,age=None):
         result = []
    
         for u in users:
             if name is not None and age is not None:
                 if u["name"] == name and u["age"] == age:
                     result.append(u)
                 #이름도 있고 나이도 있음
             elif name is not None:
                 if u["name"] == name:
                        result.append(u)
             elif age is not None:
                 if u["age"] == age:
                    result.append(u)
             else: 
                result.append(u)
    
    