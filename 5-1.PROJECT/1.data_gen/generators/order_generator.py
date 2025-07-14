import uuid
import random
from generators.user.date_generator import DateTimeGenerator

class OrderGenerator:
    def __init__(self, user_id,store_id): #uuid 가져오기
        self.user_id = user_id
        self.store_id = store_id
        self.datetime_gen = DateTimeGenerator()
        
    def generate_orders(self,count):
        orders = []
        
        for _ in range(count):
            order_id = str(uuid.uuid4())
            ordered_at =  self.datetime_gen.generate_datetime()
            user_id = random.choice(self.user_id)
            store_id = random.choice(self.store_id)
        
            orders.append({
            "id" : order_id,
            "ordered_at" : ordered_at,
            "user_id" : user_id,
            "store_id" : store_id
          })

        return orders
            
            