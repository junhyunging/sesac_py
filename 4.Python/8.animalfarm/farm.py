from typing import List
from animal import Animal

class Farm(Animal):
    def __init__(self):
        self._animals : List[Animal] = []

    def add_animal(self,animal):
        self._animals.append(animal)
        print(f"{self._name}이 농장에 방문했습니다.")
    
    def feed_all(self):
        print("동물들에게 밥주는중")
        for animal in self._animals:
            animal.feed("food")
        
 
    # def show_all(self):
        
        
        