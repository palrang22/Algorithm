n, m = map(int, input().split())
lst_a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
lst_b = [list(map(int, input().split())) for _ in range(m)]
lst_new = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m):
            lst_new[i][j] += lst_a[i][t] * lst_b[t][j]

for row in lst_new:
    print(*row)