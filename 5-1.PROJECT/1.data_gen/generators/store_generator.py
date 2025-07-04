import uuid
import random

class StoreGenerator:
    def __init__(self,brand_file_path):
        self.brand_names = self.load_brands(brand_file_path)
        
        #주요 지역
        self.regions =[
            "홍대","강남","명동","연남","성수","합정","이태원","망원","문래"
        ]
        
    def load_brands(self,file_path):
        with open(file_path, "r",encoding="utf-8") as file:
            return file.read().splitlines()
    
    def generate_address(self):
        gu = random.choice(["마포구","용산구","중구","서대문구","강남구","송파구","서초구","성북구"])
        street_num = random.randint(1,99)
        road_num = random.randint(1,50)
        patandmat = random.choice(["길","로"])
        return f"서울 {gu} {street_num}{patandmat} {road_num}"
    
    def generate_stores(self,count):
        stores = []
        for _ in range(count):
            store_id = str(uuid.uuid4()) #str로 감싸지 않으면 UUID 뜸.. 문자여로
            brand = random.choice(self.brand_names)
            regions = random.choice(self.regions)
            brand_num = random.randint(1,10) #매장 번호
            store_name = f"{brand} {regions}{brand_num}호점"
            address = self.generate_address()
            
            stores.append({
                "id" : store_id,
                "type" : brand,
                "name" : store_name,
                "address" : address
            })            
        return stores

    
        
        
        