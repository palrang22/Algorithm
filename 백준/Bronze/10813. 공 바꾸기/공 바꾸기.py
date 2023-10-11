N, M= map(int, input().split())
lst = []

for i in range(N):
    lst.append(i+1)

for b in range(M):
    i, j = map(int, input().split())
    k = lst[i-1]
    lst[i-1] = lst[j-1]
    lst[j-1] = k

for j in lst:
    print(j, end= " ")