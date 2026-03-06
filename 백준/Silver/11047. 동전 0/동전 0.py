import sys
input = sys.stdin.readline

n, k = map(int, input().split(" "))
coin_lst = sorted([int(input()) for _ in range(n)], reverse=True)
count = 0

for i in coin_lst:
    count += k // i
    k = k % i

print(count)
