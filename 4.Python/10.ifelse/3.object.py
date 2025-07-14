class User:
    pass

class Store:
    pass

class Item:
    pass

class DisplayData :
    def __init__(self,data):
        self.handlers = {
            str: self.display_user,
            list: self.display_store,
            dict: self.display_item
            #새로운 타입을 여기에 추가
        }
        handler = self.handlers.get(type(data), self.unsupported_type) # .get()은 있으면 반환, 없으면 기본값을 두번째 인자로.
        handler(data)
        
    def display_user(self,data):
        print(f"문자열",{data})
    def display_store(self,list):
        print(f"문자열",{list})
    def display_item(self,dict):
        print(f"문자열",{dict})
    def unsupported_type(self):
        print("지원 x")
        
DisplayData(User())
DisplayData(Store())
DisplayData(Item())
