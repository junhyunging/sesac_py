from generators.user_generator import UserGenerator

user_gen = UserGenerator("lastName.txt","firstName.txt")

users = user_gen.generate_users(1000)

for user in users:
    print(user)