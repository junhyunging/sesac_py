import random

class NameGenerator:
    def __init__(self,last_file_path,first_file_path):
        self.last_names = self.load_data_from_file(last_file_path)
        self.first_names = self.load_data_from_file(first_file_path)
        
    def load_data_from_file(self,file_path):
        with open(file_path,'r',encoding='utf-8') as file:
            return file.read().splitlines()
    
    def generate_name(self):
        last = random.choice(self.last_names)
        first = random.choice(self.first_names)
        return f"{last}{first}"
