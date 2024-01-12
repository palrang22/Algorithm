dud = set()
bo = set()

d, b = map(int, input().split())

for _ in range(d):
    dud.add(input())
for _ in range(b):
    bo.add(input())

dudbo = list(dud & bo)
dudbo.sort()

print(len(dudbo))

for j in dudbo: print(j)