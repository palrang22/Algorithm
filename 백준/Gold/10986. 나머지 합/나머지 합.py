import sys
input = sys.stdin.readline

n, m = map(int, input().split())
prefix_sum = [0] * n
lst = list(map(int, input().split()))

prefix_sum[0] = lst[0] % m

for i in range(n):
    if i >= 1:
        prefix_sum[i] = (prefix_sum[i-1] + lst[i]) % m

count = [0 for _ in range(m)]
ans = 0


for i in prefix_sum:
    count[i] += 1

for j in range(m):
    if j == 0:
        ans += count[j]
    cnt = count[j]
    ans += cnt * (cnt-1) // 2

print(ans)