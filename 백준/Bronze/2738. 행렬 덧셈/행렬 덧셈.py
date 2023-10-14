N, M = map(int, input().split())
a_square = []
b_square = []

for i in range(N):
  a = list(map(int, input().split()))
  a_square.append(a)

for j in range(N):
  b = list(map(int, input().split()))
  b_square.append(b)

for n in range(N):
  for m in range(M):
    sum = a_square[n][m] + b_square[n][m]
    print(sum, end = ' ')
  print()