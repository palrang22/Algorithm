import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lst = sorted(list(map(int, input().split(" "))))

res = []

visited = [False]*n

def backtracking(cur: int):
    if len(res) == m:
        print(*res)
        return
    
    prev = None
    
    for i in range(cur, n):
        if visited[i]:
            continue

        if prev == lst[i]:
            continue

        res.append(lst[i])
        visited[i] = True
        prev = lst[i]

        backtracking(i)

        res.pop()
        visited[i] = False

backtracking(0)