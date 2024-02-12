import sys
input = sys.stdin.readline

N = int(input())

def star(x):
    lst = []
    if x == 1:
        return '*'
    else:
        x = x//3
        for i in star(x):
            lst.append(i*3)
        for j in star(x):
            lst.append(j + ' '*x + j)
        for k in star(x):
            lst.append(k*3)     
    return lst

for l in star(N):
    print(l)