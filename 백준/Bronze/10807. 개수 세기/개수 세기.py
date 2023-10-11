N = int(input())

lst = list(map(int, input().split()))

v = int(input())

num = 0

for i in lst:
    if i == v:
        num += 1
        
print(num)