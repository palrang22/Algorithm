import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lst = sorted(list(map(int, input().split(" "))))


res = []

def backtracking(cur: int):
    if len(res) == m:
        res_str = list(map(str, res))
        print(" ".join(res_str))
        return
    
    for i in range(cur, n):
        if lst[i] not in res:
            res.append(lst[i])
            backtracking(cur)
            res.pop()
        cur += 1

backtracking(0)