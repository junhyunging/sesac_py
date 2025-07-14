import uuid
import datetime

from generators.user.name_generator import NameGenerator
from generators.user.gender_generator import GenderGenerator
from generators.user.birthday_generator import BirthdayGenerator

class UserGenerator:
    def __init__(self,last_name_file,first_name_file):
        self.name_gen = NameGenerator(last_name_file,first_name_file)
        self.gender_gen = GenderGenerator()
        self.bday_gen = BirthdayGenerator()
        
    #나이 계싼
    def create_age(self,birthday):
        birth = datetime.datetime.strptime(birthday, "%Y-%m-%d")    #strptime 문자열 -> datetime 객체로 strftime datetime -> 문자열
        today = datetime.datetime.today()
        age = today.year - birth.year
        
        #생일 안 지낫으면 한살뺴주기
        if today.month < birth.month:
            age -= 1
        return age
    
    def generate_users(self, count):
        users = [] #여기에 저장
        
        for _ in range(count):
            user_id = str(uuid.uuid4()) # 고유 id 
            name = self.name_gen.generate_name()
            gender = self.gender_gen.generator_gender()
            birthday = self.bday_gen.generate_birthday()
            age = self.create_age(birthday)
            
            #저장하기
            users.append({
                "id" : user_id,
                "name" : name,
                "gender" : gender,
                "age" : age,
                "birthday" : birthday
            })
        
        return users
            
            
            
                    
        