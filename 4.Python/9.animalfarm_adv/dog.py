from animal import Animal

class Dog(Animal):
    
    # def speak(self):
    #     return "Woof"
    sound = "wall"
        
    def move(self):
        if self._energy >= 10:
            self._energy -= 10
            print(f"{self._name} 에너지가 줄어들었습니다." )
        else:
            print(f"{self._name}에너지가 없습니다.")
        
            

        
    
    