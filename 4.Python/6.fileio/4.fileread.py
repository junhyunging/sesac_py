import csv

file_path = "text.csv"

data= []

with open(file_path,"r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # print(row)
        data.append(row)
        
print(data)



