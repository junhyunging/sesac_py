import random

class TypeGenerator:
    def __init__(self):
        self.types = ["coffee","cake","juice"]
        
    def generate_type(self):
        return random.choice(self.types)