import uuid
import random

class OrderItemGenerator:
    def __init__(self,order_id,item_id):
        self.order_id = order_id
        self.item_id = item_id
    
    def generate_orderitem(self,count):
        orderitems = []
        
        for _ in range(count):
            order_id = random.choice(self.order_id)
            item_id = random.choice(self.item_id)
        
            orderitems.append({
                "id" : str(uuid.uuid4()),
                "order_id" : order_id,
                "item_id" : item_id
            })
            
        return orderitems
            