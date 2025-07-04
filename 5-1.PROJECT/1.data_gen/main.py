import sys
import csv

from generators.user_generator import UserGenerator
from generators.order_generator import OrderGenerator
from generators.orderitem_generator import OrderItemGenerator
from generators.item_generator import ItemGenerator
from generators.store_generator import StoreGenerator

class DisplayData:
    def __init__(self):
        self.user_gen = UserGenerator("lastName.txt","firstName.txt")
        self.store_gen = StoreGenerator("brand.txt")
        self.item_gen = ItemGenerator()

        # 꺼낼수있게 저장
        self.users = []
        self.stores = []
        self.items = []
        self.orders= []
    
    def generate(self,data_type,count):
        if data_type == "user":
            self.users = self.user_gen.generate_users(count)
            return self.users
        elif data_type == "store":
            self.stores = self.store_gen.generate_stores(count)
            return self.stores
        elif data_type == "item":
            self.items = self.item_gen.generate_items(count)
            return self.items
        #user와 store에서 id값 뽑아오기
        elif data_type == "order":
            #id 값을 user와 store에서 가져오려고 하는데 없다고 해서 오류가 남 so 다시 만들기
            if not self.users:
             self.users = self.generate("user",count)
            if not self.stores:
             self.stores = self.generate("store",count)
             
            user_ids = []
            for user in self.users:
                user_ids.append(user["id"]) #아이디만 가져오기
            store_ids = []
            for store in self.stores:
                store_ids.append(store["id"])
            
            self.order_gen = OrderGenerator(user_ids,store_ids)
            return self.order_gen.generate_orders(count)
        
        #위와똑가티 order,item
        elif data_type == "orderitem":
            if not self.orders:
                self.orders = self.generate("order", count)
            if not self.items:
                self.items = self.generate("item", count)
            
            order_ids = []
            for order in self.orders:
                order_ids.append(order["id"]) #아이디만 가져오기
            item_ids = []
            for item in self.items:
                item_ids.append(item["id"])
            
            self.orderitem_gen = OrderItemGenerator(order_ids,item_ids)
            return self.orderitem_gen.generate_orderitem(count)
        
        else :
            print("똑바로 입력하십숑")
            return []
        
# 데이터 입력받기        
if len(sys.argv) > 1:
    data_type = sys.argv[1]
else : 
    data_type = input("데이터를 입력해주세요 (user,store,item,order,orderitem) :")

#숫자 입력받기    
if len(sys.argv) > 2:
    count = int(sys.argv[2])
else :
    count = int(input("숫자를 입력하세요 : "))

if len(sys.argv) > 3:
    output_format = sys.argv[3]
else :
    output_format = input("출력 형식은? console, csv : ")
    
my_data = DisplayData()
data = my_data.generate(data_type,count)

if output_format == "console":
    for item in data:
        print(item)

elif output_format == "csv":
    if data:
        keys = data[0].keys() # 첫번째 딕셔너리에서 key들만 가져옴
        filename = f"{data_type}.csv"
        with open(filename,"w",newline="",encoding="utf-8") as file: #한국어 설정 줄바꿈
            writer = csv.DictWriter(file,fieldnames=keys)
            writer.writeheader() #첫줄에 key들의 이름
            writer.writerows(data)
        print(f"{filename}파일이 저장되었습니다.")
    else:
        print("x")
    

    



    
        
                    