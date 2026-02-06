import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
res = []

def backtracking():
    if len(res) == m:
        print(" ".join(map(str, res)))
        return

    for i in range(1, n+1):
        res.append(i)
        backtracking()
        res.pop()

backtracking()