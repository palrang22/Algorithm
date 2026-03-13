import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
sum_set = set()

p_left = 0
p_right = 0+k-1
current = sum(lst[p_left:p_left + k])
ans = current

while p_right < n-1:

    current = current - lst[p_left] + lst[p_right+1]
    ans = max(ans, current)

    p_left, p_right = p_left + 1, p_right + 1

print(ans)