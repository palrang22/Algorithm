li = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0
ind = 0

N, B = map(str, input().split())
B = int(B)
N = list(N)
N.reverse()

for i in N:
    each = (B ** ind) * (i:=li.index(i))
    sum += each
    ind += 1

print(sum)