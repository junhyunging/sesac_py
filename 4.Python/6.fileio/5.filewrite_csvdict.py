#CSV 파일은 ?? comma sepreated value
import csv

file_path = "text.csv"

data = [
    {"Name" : 'John', "Age":25,"City": 'Seoul'},
    {"Name" :'Jane',"Age": 88,"City":'Busan'},
    {"Name" :'Bob',"Age": 30,"City":'Jeju'},
]

print(data)
for person in data:
    # for key,value in person.items()
    print(person)
        # print(f"key : {key} vlaue : {value}")
    
    
with open(file_path, "w", newline="") as file:
    # headers = ["Name","Age","City"]
    headers = data[0].keys()
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(data)
    csv_writer.writerow(['Alice',40,'Suwon'])