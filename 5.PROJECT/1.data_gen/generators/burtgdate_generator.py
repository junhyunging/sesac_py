import random
import datetime as dt

class BirthdateGenerator:
    def generate_birthdate(self):
        year = random.randint(1990, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"
    
    def generate_age(self):
        now = dt.datetime.now().strftime('%Y')
        
    