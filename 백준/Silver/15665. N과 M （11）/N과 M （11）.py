import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lst = sorted(set(list(map(int, input().split(" ")))))

res = []

def backtracking():
    if len(res) == m:
        print(*res)
        return
    
    for i in lst:
        res.append(i)
        backtracking()
        res.pop()

backtracking()