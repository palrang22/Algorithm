import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [0] * n

for i in range(n):
    if i == 0:
        dp[0] = lst[0]
    if i == 1:
        dp[1] = lst[0] + lst[1]
    if i == 2:
        dp[2] = max(lst[0]+lst[1], lst[0]+lst[2], lst[1]+lst[2])
    
    if i >= 3:
        dp[i] = max(dp[i-1], dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i])


print(dp[-1])