def print_coin():
    print("비트코인")

print_coin()

for i in range(100):
    print_coin()
    
def  print_coins():
    for i in range(100):
        print("비트코인")

def hello ():
    print("Hi") 

hello()       

def  print_with_smile(string):
    print(string + ":D")
    
print_with_smile("안녕하세욤")

def print_upper_price(price):
    print(price * 1.3)
    
print_upper_price(300)

def print_sum(a,b):
    print(a + b)
    
print_sum(1,4)

def print_arithmetic_operation (a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    
def  print_max(a,b,c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
        
    print(max_val)  

print_max(19,11,7)
   
def print_reverse(string):
    print(string[::-1]) #[::-1 역순으로 뽑는거]
    
print_reverse("Pyton")    

def print_score(score_list):
    print(sum(score_list)/len(score_list))
    
print_score([4,5,6])    

#223
    
def print_even(sum_list):
    for s in sum_list:
        if s % 2 == 0 :
            print(s)
            
print_even([1,4,5,24,5])

def print_keys(dic):
    for keys in dic.keys():
        print(keys)
        
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

import datetime

now = datetime.datetime.now()

today = datetime.datetime.today()

myNow = (now-datetime.datetime.today.year+1)


print(myNow)

print(now)

def simple_interest(num):
    for number in num.keys():
        if number>10
        print(f"{number}")
        
        
    
    











            
    