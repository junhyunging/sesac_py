class DisplayData :
    def __init__(self,data):
        if isinstance(data,'str'):
            self.display_str(data)
        elif isinstance(data,'list'):
            self.display_list(data)
        elif isinstance(data,'dict'):
            type.display_dict(data)
        else :
            raise TypeError("ㅋlㅋl")
        
    def display_str(self,data):
        print(f"문자열",{data})
    def display_list(self,list):
        print(f"문자열",{list})
    def display_dict(self,dict):
        print(f"문자열",{dict})
        
