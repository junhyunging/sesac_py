class Person:
    def __init__(self,name,age):
        self._name = name #속성 (Attribute) - __ 밑 줄 두개는 private 속성이라서, 클라스 밖에선 바꾸지 못하게 함
        self._age = age #속성 (Attribute) 
        
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        self._name = name
    
    def get_age(self):
        return self._age
    
    def set_age(self,age):
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

print(person1.get_name())
person1.set_name("박철순")
print(person1.get_name())
