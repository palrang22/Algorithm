import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lst = [list(map(int, input().split())) for _ in range(n)]
sum = 0
dp = [[0]*(n+1) for _ in range(n+1)]


for i in range(n+1):
    for j in range(n+1):
        if i>0 and j>0:
            dp[i][j] = lst[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            continue

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])