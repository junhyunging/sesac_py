class User:
    def display(self):
        print("사용자처리")

class Store:
    def display(self):
        print("상점 객체")

class Item:
    def display(self):
        print("아이템 객체")


class DisplayData :
    def __init__(self,data):
        data.display()
        
DisplayData(User())
DisplayData(Store())
DisplayData(Item())
#중간 중계자를 이용해 oop처리