
N, M = map(int, input().split())

lst = []

for n in range(N):
    lst.append(n+1)

for m in range(M):
    i, j = map(int, input().split())
    range_list = []
    for m in range(i-1, j):
        range_list.append(lst[m])
        
    reversed_list = list(reversed(range_list))

    ii = 0

    for o in range(i-1, j):
        lst[o] = reversed_list[ii]
        ii += 1
        
for i in lst:
    print(i, end = ' ')