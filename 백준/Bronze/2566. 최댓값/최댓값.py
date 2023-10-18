alllist=[]
maxlist = []

for i in range(9):
    a = list(map(int, input().split()))
    maxlist.append(max(a))
    alllist.append(a)

maxmax = max(maxlist)
maxrow = maxlist.index(maxmax)
maxcol = alllist[maxrow].index(max(maxlist))

print(maxmax)
print(maxrow+1, maxcol+1)