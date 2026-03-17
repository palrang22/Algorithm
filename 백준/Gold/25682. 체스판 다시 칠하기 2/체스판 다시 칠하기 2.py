import sys
input = sys.stdin.readline

def main():

    n, m, k = map(int, input().split())
    board = [input().rstrip() for _ in range(n)]
    new_board = []

    for i in range(n):
        row = []
        for j in range(m):
            stone = board[i][j]
            if (i+j) % 2 == 0:
                row.append(1) if stone == "B" else row.append(0)
            else:
                row.append(1) if stone == "W" else row.append(0)
        new_board.append(row)

    for i in range(n):
        for j in range(m):
            if i > 0:
                new_board[i][j] += new_board[i-1][j]
            if j > 0:
                new_board[i][j] += new_board[i][j-1]
            if i > 0 and j > 0:
                new_board[i][j] -= new_board[i-1][j-1]

    ans = k*k

    for i in range(n-k+1):
        for j in range(m-k+1):
            x1, y1, x2, y2 = i, j, i+k-1, j+k-1

            count = new_board[x2][y2]

            if x1 > 0:
                count -= new_board[x1-1][y2]
            if y1 > 0:
                count -= new_board[x2][y1-1]
            if x1>0 and y1>0:
                count += new_board[x1-1][y1-1]

            ans = min(ans, count, k**2 - count)

    print(ans)

main()