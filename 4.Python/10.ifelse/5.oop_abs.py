from abc import ABC, abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

class User(Displayable):
    def display(self):
        print("사용자처리")

class Store(Displayable):
    def display(self):
        print("상점 객체")

class Item(Displayable):
    def display(self):
        print("아이템 객체")

class Order(Displayable):
    def display(self): #이걸 강제로 하도록 만ㄷ륵
        print("오더 객체")


class DisplayData :
    def __init__(self,data):
        data.display()
        
DisplayData(User())
DisplayData(Store())
DisplayData(Item())
#중간 중계자를 이용해 oop처리