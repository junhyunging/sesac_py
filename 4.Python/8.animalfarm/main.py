#Animal 클래스를 만들고,
#상속받은 Cat,Dog 를 만든다
#각각의 동물들은 이름과 에너지를 갖고 있음.
#각각의 동물들은 speak(),move()

#고양이는 Meow
#멍멍이는 Woof

#고양이는 움직일때마다 에너지가 5씩 줄어든다
#멍멍이는 움직일때마다 에너지가 10씩 줄어든다.

#Farm 이라는 클래스를 만들고
#여기 농장에는 동물들을 추가
#add_animal 함수를 통해서 동물을 농장에 추가한다.
#밥주기: feed_all 함수 통해서 모든 동물 밥주기 (+50에너지 추가)
#놀기 : play_all

from cat import Cat
from dog import Dog
from animal import Animal
from farm import Farm

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("kitty")
    
    farm = Farm()
    farm.add_animal(dog)
    farm.add_animal(cat)
    
    print(dog.speak())
    print(cat.speak())
    
    dog.move()
    cat.move()
    
    #반복문을 통해서 10번 움직인다.
    for i in range(10):
        dog.move()
    
    farm.feed_all()
        

    
