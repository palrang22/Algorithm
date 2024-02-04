import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
sumList = [0]
sum = 0

for a in num:
    sum += a
    sumList.append(sum)
    
for _ in range(M):
    i, j = map(int, input().split())

    print(sumList[j]-sumList[i-1])