import random
names = ['John','Jane','Michael','Emily','William','Olivia']
cities = ['New York','Los Angeles','Chicago','Houston','Philadelphia']

def generate_name():
    return random.choice(names)

def generate_birthdate():
    year = random.randint(1990,2010)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return f"{year}-{month:02d}-{day:02d}"    

print(generate_name())
print(generate_birthdate())

def generate_gender():
    return random.choice("Male","Female")

def generate_address():
    city = random.choice(cities)
    street_num = random.randint(1,100)
    return f"{street_num} {city}"

users = []
for _ in range(10):
    name = generate_name()
    bday = generate_birthdate()
    users.append((name,bday))
    gender = generate_gender()
    address = generate_address()
    
for u in users:
    print(u)
    