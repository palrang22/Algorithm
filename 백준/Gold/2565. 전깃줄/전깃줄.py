import sys
input = sys.stdin.readline


n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split(" "))
    lst.append((a, b))
lst.sort(key=lambda x: x[0])

b_lst = []
for a, b in lst:
    b_lst.append(b)

dp = [1]*n


for i in range(n):
    for j in range(i):
        if b_lst[j] < b_lst[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))