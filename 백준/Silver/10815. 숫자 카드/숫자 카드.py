n = int(input())
set = set(map(int, input().split(" ")))
m = int(input())
lst = list(map(int, input().split(" ")))

return_lst = []

for i in lst:
    if i in set:
        return_lst.append(1)
    else:
        return_lst.append(0)

print(" ".join(map(str, return_lst)))