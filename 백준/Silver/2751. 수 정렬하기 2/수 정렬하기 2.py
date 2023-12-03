import sys
n_row = int(input())
list_row=[]

for i in range(n_row):
    row = int(sys.stdin.readline())
    list_row.append(row)

list_row.sort()

for j in list_row:
    print(j)
