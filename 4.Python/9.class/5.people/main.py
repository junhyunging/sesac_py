# import person
from person import Person
from student import Student
from employee import Employee

Alice = Person("Alice",23)
Bob = Person("Bob",24)
tom = Student("Tom",20,"S123456")
charlie = Employee("Charlie",31,"Samsung")


Alice.greet()
Bob.greet()
Bob.name = "BOB"
Bob.greet

tom.greet()
tom.study()

charlie.greet()
charlie.work()