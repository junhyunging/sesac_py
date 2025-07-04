import random
class PriceGenerator:
    def generate_price(self):
        return random.randint(6,16) * 500 #최소 3000원에서 8000원 500원 단위
    