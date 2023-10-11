X = int(input())
N = int(input())

X_real = 0

for i in range(N):
    a, b = map(int, input().split())
    X_real += a * b

if X == X_real:
    print("Yes")
else:
    print("No")