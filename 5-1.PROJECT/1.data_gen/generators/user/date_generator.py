import random

class DateTimeGenerator:
    def generate_datetime(self):
        year = random.randint(2023,2025)
        month = random.randint(1,12)
        day = random.randint(1,28)
        
        hour = random.randint(2,23)
        minute = random.randint(0,59)
        second = random.randint(0,59)
        
        return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
    
#테스트
# if __name__ == "__main__":
#     time = DateTimeGenerator()
#     for _ in range(1):
#         print(time.generate_datetime())