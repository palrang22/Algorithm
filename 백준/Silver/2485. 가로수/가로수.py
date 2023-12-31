import sys

input = sys.stdin.readline

def gcd_of_list(*args):
    result = args[0]
    
    for num in args[1:]:
        result = gcd(result, num)
    
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

N = int(input())
lst = [int(input()) for _ in range(N)]
minusList = [-lst[i-1] + lst[i] for i in range(1, N)]

lenNum = lst[-1] - lst[0]
numTree = (lenNum // gcd_of_list(*minusList)) + 1

print(numTree - len(lst))