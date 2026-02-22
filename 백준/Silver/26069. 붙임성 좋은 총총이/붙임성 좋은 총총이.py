import sys
input = sys.stdin.readline

dancing = set()
dancing.add("ChongChong")

n = int(input())

for _ in range(n):
    a, b = input().rstrip().split(" ")

    if a in dancing:
        dancing.add(b)
        continue

    if b in dancing:
        dancing.add(a)

print(len(dancing))