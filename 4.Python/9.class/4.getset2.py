class Person:
    def __init__(self,name,age):
        self._name = name #속성 (Attribute) - __ 밑 줄 두개는 private 속성이라서, 클라스 밖에선 바꾸지 못하게 함
        self._age = age #속성 (Attribute) 
    
    @property       # 이 함수는 getter입니다..    
    def name(self):
        return self._name
    
    @name.setter  # 이 함수는 setter입니다.
    def name(self,name):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if age >= 0:
            self._age = age
        else:
            print("나이는 0보다 커야 합니다.")
        
    def greet(self): #메소드 (Method - 객체함수)
        print(f"안녕하세용, 저는 {self._name}입니다.")

    def ride_car(self): #메소드 (Method - 객체함수)
        print(f"자동차를 탑니다")

person1 = Person("김철수",30)
person2 = Person("신준형",25)

print(person1.name) # setter/getter 를 파이썬 신버전에서 decorater로 지정을 했으면, 함수가 아닌 변수처럼 쉽게 접근할수잇음

print(person1.age)

person1.name = "박민관"
person1.age = 35

print(person1.age)

person1.age = -110

# 이 최신 ㅏ이썬 문법으로 짜면?? 객체 안에 변수를 자유롭게 바꾸는 것처럼 보이지만,
# 실제로는 함수를 통해서, 에러 처리 등등을 통과해서 할당되는 매~우 재밌는(?) 구조임.
