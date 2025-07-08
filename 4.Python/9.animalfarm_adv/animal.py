from abc import ABC , abstractmethod

class Animal:
    def __init__(self,name):
        self._name = name
        self._energy = 100

    # @abstractmethod
    # def speak(self):
    #     pass
    # @abstractmethod
    # def move(self):
    #     pass
    
    def speak(self):
        print(f"{self._name}사운드{self.speak_style()}")
        
    def speak_style(self):
        if self._energy >=80:
            return self.sound.upper()
        else :
            return "..."
    
    def feed(self, food:str) -> None:
        self._energy += 50
        print(f"{self._name}는 푸드를 먹었습니다. 잔여 에너지 {self._energy}")