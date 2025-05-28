length, width = map(int, input().split())
board = []

for _ in range(length):
    board.append(list(input()))

count = []

for i in range(length-7):
    for j in range(width-7):
        count_start_B = 0
        count_start_W = 0
        for x in range(8):
            for y in range(8):
                current = board[i+x][j+y]

                if (x+y)%2 == 0:
                    if current == "B":
                        count_start_W += 1
                    else:
                        count_start_B += 1
                else:
                    if current == "W":
                        count_start_W += 1
                    else:
                        count_start_B += 1
                
        count.append(min(count_start_B, count_start_W))
                
print(min(count))