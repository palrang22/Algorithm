          
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

camp = [list(input().rstrip()) for _ in range(N)]

def bfs(camp, n, m):
    q = deque()
    camp[n][m] = 'V'
    q.append((n, m))
    count = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and camp[nx][ny] != 'X':
                if camp[nx][ny] != 'V':
                    if camp[nx][ny] == 'P':
                        count += 1
                    camp[nx][ny] = 'V'
                    q.append((nx, ny))
                    
    if count != 0:
        return count
    else:
        return 'TT'

for i in range(N):
    for j in range(M):
        if camp[i][j] == 'I':
            print(bfs(camp, i, j))
            break
