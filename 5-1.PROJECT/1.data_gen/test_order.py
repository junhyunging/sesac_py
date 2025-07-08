from generators.user_generator import UserGenerator
from generators.store_generator import StoreGenerator
from generators.order_generator import OrderGenerator

user_gen = UserGenerator("lastName.txt", "firstName.txt")
store_gen = StoreGenerator("brand.txt")

users = user_gen.generate_user(100)
stores = store_gen.generate_stores(100)

user_id = [user["id"] for user in users]
store_id = [store["id"] for store in stores]

order_gen = OrderGenerator(user_id, store_id)
orders = order_gen.generate_orders(100)

for order in orders:
    print(order)