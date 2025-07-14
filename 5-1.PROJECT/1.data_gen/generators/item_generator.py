import uuid
from generators.item.food_generator import FoodGenerator
from generators.item.type_generator import TypeGenerator
from generators.item.price_generator import PriceGenerator

class ItemGenerator:
    def __init__(self):
        self.type_gen = TypeGenerator()
        self.food_gen = FoodGenerator()
        self.price_gen = PriceGenerator()
    
    def generate_items(self,count):
        items = []
        for _ in range(count):
            item_id = str(uuid.uuid4())
            item_type = self.type_gen.generate_type()
            food = self.food_gen.generate_food(item_type)
            price = self.price_gen.generate_price()
            
            items.append({
                "id" : item_id,
                "type" : item_type,
                "name" : food,
                "unit_price" : price
        })
        return items
        