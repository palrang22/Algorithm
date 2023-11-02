list_a = []
list_b = []

for i in range(3): 
    a, b = map(int, input().split())
    list_a.append(a)
    list_b.append(b)

for j in list_a:
    if list_a.count(j) == 1 :
        print(j, end=' ')
        break
    else:
        continue

for k in list_b:
    if list_b.count(k) == 1 :
        print(k)
        break
    else:
        continue