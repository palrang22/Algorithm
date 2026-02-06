import sys
input = sys.stdin.readline

n = int(input())

res = [False] * n
left_diag = [False] * (2*n-1)
right_diag = [False] * (2*n-1)

count = 0

def backtracking(row: int):
    global count

    if row == n:
        count += 1
        return
    
    for col in range(n):
        ld = row+col
        rd = row-col

        if res[col] or left_diag[ld] or right_diag[rd]:
            continue

        res[col] = True
        left_diag[row+col] = True
        right_diag[row-col] = True

        backtracking(row+1)
        
        res[col] = False
        left_diag[row+col] = False
        right_diag[row-col] = False

backtracking(0)
print(count)