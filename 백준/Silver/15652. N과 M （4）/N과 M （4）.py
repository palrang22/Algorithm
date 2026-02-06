import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
res = []

def backtracking(cur: int):
    if len(res) == m:
        print(" ".join(map(str, res)))
        return

    for i in range(1, n+1):
        if len(res) == 0:
            cur += 1
            res.append(i)
            backtracking(cur)
            res.pop()
        else:
            if res[-1] <= i:
                cur += 1
                res.append(i)
                backtracking(cur)
                res.pop()

backtracking(1)