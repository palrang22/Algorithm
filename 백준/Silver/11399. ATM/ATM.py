import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
time.sort()
eachtime = []
a = 0

for i in time:
    a += i
    eachtime.append(a)

print(sum(eachtime))