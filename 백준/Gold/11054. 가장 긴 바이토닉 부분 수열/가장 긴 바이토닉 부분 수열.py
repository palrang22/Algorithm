import sys
input = sys.stdin.readline


n = int(input())
lst = list(map(int, input().split(" ")))
dp = [1]*n
dp_down = [1]*n


for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if lst[j] < lst[i]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)

rtr = 0
for i in range(n):
    rtr = max(rtr, dp[i] + dp_down[i] - 1)

print(rtr)