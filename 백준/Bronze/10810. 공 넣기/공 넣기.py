N, M= map(int, input().split())
lst = []

for i in range(N):
    lst.append(0)

for i in range(M):
    a, b, c = map(int, input().split())
    
    for i in range(a-1,b):
        lst[i] = c

for j in lst:
    print(j, end = " ")