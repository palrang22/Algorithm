square = [[0 for col in range(100)] for row in range(100)]
black = 0

N = int(input())

for i in range(N):
    x, y = map(int, input().split())
    for a in range(x,x+10):
        for b in range(y, y+10):
            if square[a][b] != 1 :
                square[a][b] = 1
                black += 1
            else:
                continue
            
print(black)