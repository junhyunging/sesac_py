class DisplayData :
    def __init__(self,data):
        self.handlers = {
            str: self.display_str,
            list: self.display_list,
            dict: self.display_dict
            #새로운 타입을 여기에 추가
        }
        handler = self.handlers.get(type(data), self.unsupported_type) # .get()은 있으면 반환, 없으면 기본값을 두번째 인자로.
        handler(data)
        
    def display_str(self,data):
        print(f"문자열",{data})
    def display_list(self,list):
        print(f"문자열",{list})
    def display_dict(self,dict):
        print(f"문자열",{dict})
    def unsupported_type(self,data):
        print("지원 x")
        
DisplayData("hello")
DisplayData([1,2,3])
DisplayData("hello")
