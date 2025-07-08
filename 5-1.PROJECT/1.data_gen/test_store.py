from generators.store_generator import StoreGenerator

store_gen = StoreGenerator("brand.txt")

stores = store_gen.generate_stores(100)

for store in stores:
    print(store)
    
    
