#CSV 파일은 ?? comma sepreated value
import csv

file_path = "text.csv"

data = [
    ['Name','Age','City'],
    ['John',25,'Seoul'],
    ['Jane',88,'Busan'],
    ['Bob',30,'Jeju'],
]

print(data)
for i in range(len(data)):
    print(data[i])
    
with open(file_path, "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    csv_writer.writerow(['Alice',40,'Suwon'])

print("CSV 쓰기 완료")