li = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
changed = []

N, B = map(int, input().split())

while True:
    a = li[N % B]
    changed.append(a)
    N = N//B
    
    if N == 0:
        break
    
for i in changed[::-1]: print(i, end='')