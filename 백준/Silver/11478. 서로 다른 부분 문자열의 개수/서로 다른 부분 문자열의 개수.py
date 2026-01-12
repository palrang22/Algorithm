import sys
input = sys.stdin.readline

n = input()
m = len(n)

target = set()

for i in range(0, m):
    for j in range(1, m-i):
        target.add(n[i:i+j])

print(len(target))