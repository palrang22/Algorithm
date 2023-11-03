a = list(map(int, input().split()))

if max(a)*2 < sum(a):
    print(sum(a))

else:
    print((sum(a)-max(a))*2 -1)