def numOfDigits(num):
    numOfDigits(12345)
    print(len(str(num)))
    
def gugu(m):
    for n in range(1,9):
        print(f"{m} * {n}' = {m*n:2d}")
        
    c = gugu(3)
    print(c)
    
    
def simple_interest(p,r,t):
    
    return int(p*r*t)

def simple_interest_amount(p,r,t):
    
    return int(p(1+r*t))


print(simple_interest(1000000,0.03875,5))
print(simple_interest_amount(11000000,0.05,5))

def read(text):

    return ridename, cmmin, cmmax

if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
    

