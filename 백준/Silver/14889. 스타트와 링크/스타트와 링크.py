import sys
input = sys.stdin.readline

def backtracking(depth, start):
    if depth == n // 2:
        return calculating(selected, ij_lst)

    min_diff = float('inf')

    for i in range(start, n):
        if not selected[i]:
            selected[i] = True
            diff = backtracking(depth+1, i+1)
            min_diff = min(diff, min_diff)
            selected[i] = False

    return min_diff
    

def calculating(selected, ij_lst):
    start_score = 0
    link_score = 0
    for i in range(n):
        for j in range(i+1, n):
            if selected[i] and selected[j]:
                start_score += ij_lst[i][j] + ij_lst[j][i]
            elif not selected[i] and not selected[j]:
                link_score += ij_lst[i][j] + ij_lst[j][i]
    return abs(start_score - link_score)


n = int(input())
ij_lst = []

for _ in range(n):
    ipt = list(map(int, input().split(" ")))
    ij_lst.append(ipt)


selected = [False] * n
selected[0] = True

print(backtracking(1, 1))