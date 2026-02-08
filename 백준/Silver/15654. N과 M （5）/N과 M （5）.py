import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lst = sorted(list(map(int, input().split(" "))))


res = []

def backtracking():
    if len(res) == m:
        res_str = list(map(str, res))
        print(" ".join(res_str))
        return
    
    for i in lst:
        if i not in res:
            res.append(i)
            backtracking()
            res.pop()

backtracking()