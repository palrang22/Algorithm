import math as mt

def is_prime(x):
    if x == 1:
        return False
    else:
        for i in range (2,int(mt.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
    
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        print(2)
    else:
        while not is_prime(num):
            num+=1
        print(num)