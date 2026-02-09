import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lst = sorted(list(map(int, input().split(" "))))

res = []

visited = [False]*n

def backtracking():
    if len(res) == m:
        print(*res)
        return
    
    prev = None
    
    for i in range(n):
        if visited[i]:
            continue

        if prev == lst[i]:
            continue

        res.append(lst[i])
        visited[i] = True
        prev = lst[i]

        backtracking()

        res.pop()
        visited[i] = False

backtracking()