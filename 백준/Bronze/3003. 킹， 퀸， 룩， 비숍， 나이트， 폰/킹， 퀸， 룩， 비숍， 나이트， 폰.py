chess = [1, 1, 2, 2, 2, 8]
mine = list(map(int, input().split()))

for a, b in zip(chess, mine):
  print(a-b, end = ' ')