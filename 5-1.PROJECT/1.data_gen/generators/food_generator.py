import random
class FoodGenerator:
    def __init__(self):
        self.food_type = {
            "coffee" : ["Americano","Latte","Cappuccino","Espresso","Mocha",],
            "cake" : ["Strawberry Chocolate Cake", "Ice Box","Peach Cream Cake","Mango Cream Cake"],
            "juice" : ["Apple juice","Orange juice","Tomato juice","Lime juice","Cranberry juice"]
        }
        
    def generate_food(self,item_type):
        return random.choice(self.food_type[item_type])