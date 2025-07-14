import random

class BirthdayGenerator:
    def generate_birthday(self):
        year = random.randint(1980,2010)
        month = random.randint(1,12)
        day = random.randint(1,28)
        return f"{year:04d}-{month:02d}-{day:02d}" #자리수맞추깅 
        
