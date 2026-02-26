import sys
input = sys.stdin.readline

def backtracking(depth):
    if depth == len(empty):
        for row in sudoku:
            print(*row)
        exit()
    
    a, b = empty[depth]

    for i in range(1, 10):
        if validate(a, b, i):
            box_index = (a//3)*3+(b//3)

            sudoku[a][b] = i
            row_check[a][i] = True
            col_check[b][i] = True
            box_check[box_index][i] = True

            backtracking(depth+1)
            
            sudoku[a][b] = 0
            row_check[a][i] = False
            col_check[b][i] = False
            box_check[box_index][i] = False

def validate(a, b, value):
    box_index = (a//3)*3+(b//3)
    return not row_check[a][value] and not col_check[b][value] and not box_check[box_index][value]

sudoku = []
empty = []

row_check = [[False]*10 for _ in range(9)]
col_check = [[False]*10 for _ in range(9)]
box_check = [[False]*10 for _ in range(9)]

for i in range(9):
    row = list(map(int, input().split(" ")))
    sudoku.append(row)

    for j in range(9):
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] != 0:
            num = row[j]
            box_index = (i//3)*3+(j//3)

            row_check[i][num] = True
            col_check[j][num] = True
            box_check[box_index][num] = True


backtracking(0)