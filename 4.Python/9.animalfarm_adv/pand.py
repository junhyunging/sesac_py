from animal import Animal

class Panda(Animal):
    
    def speak(self):
        print(f"{self._name}는 PangPang 이라고 합니다.")
        
    def move(self):
        if self._energy >= 50:
            self._energy -= 50
            print(f"{self._name} 에너지가 줄어들었습니다." )
        else:
            print(f"{self._name}에너지가 없습니다.")
        
            