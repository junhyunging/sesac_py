from animal import Animal

class Cat(Animal):
    def speak(self):
        return "Meow"
    
    def move(self):
        if self._energy >= 5:
            self._energy -= 5
            print(f"{self._name} 에너지가 줄어들었습니다. 진여 에너지{self._energy}" )
        else:
            print("에너지가 없습니다.")

        
            

        
    
    