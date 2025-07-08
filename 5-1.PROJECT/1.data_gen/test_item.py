from generators.item_generator import ItemGenerator

item_gen = ItemGenerator()

items = item_gen.generate_items(20)

for item in items:
    print(item)
        