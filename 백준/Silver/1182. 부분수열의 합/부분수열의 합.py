import sys
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

def dfs(idx, total):
    if idx == n:
        return 1 if total == s else 0
    
    return dfs(idx+1, total) + dfs(idx+1, total+lst[idx])

count = dfs(0, 0)

if s == 0:
    count -= 1
    
print(count)