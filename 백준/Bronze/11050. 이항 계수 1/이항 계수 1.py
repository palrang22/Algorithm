import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
ret = 1

if n//2 < m:
    m = n-m

for i in range(m):
    ret *= (n-i)
    ret //= (i+1)

print(ret)