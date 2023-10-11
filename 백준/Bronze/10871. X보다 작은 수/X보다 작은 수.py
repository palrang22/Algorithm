import sys
count, max = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().split()))
j=[]

for i in range (1,count+1):
    if numbers[i-1] < max:
        j.append(numbers[i-1])
    else:
        i=i+1
        
print(*j)