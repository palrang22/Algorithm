
N, M = map(int, input().split())

lst = []

for n in range(N):
    lst.append(n+1)

for m in range(M):
    i, j = map(int, input().split())
    lst[i-1 : j] = lst[i-1 : j][::-1]

print(*lst)