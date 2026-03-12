import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*n

for i in range(n):
    if i <= 1:
        dp[i] = i+1
        continue
    dp[i] = (dp[i-1] + dp[i-2])%15746
    
print(dp[-1])