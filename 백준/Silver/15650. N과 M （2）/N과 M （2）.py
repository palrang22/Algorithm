import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
res = []

def backtracking(cur: int):
    if len(res) == m:
        print(" ".join(map(str, res)))
        return

    for i in range(cur, n+1):
        cur += 1
        if i not in res:
            res.append(i)
            backtracking(cur)
            res.pop()

backtracking(1)