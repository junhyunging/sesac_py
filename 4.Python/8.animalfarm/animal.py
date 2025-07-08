class Animal:
    def __init__(self,name):
        self._name = name
        self._energy = 100

    def speak(self):
        pass
    
    def move(self):
        pass
    
    def feed(self, food:str) -> None:
        self._energy += 50
        print(f"{self._name}는 푸드를 먹었습니다. 잔여 에너지 {self._energy}")