from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    farm[x][y] = 0
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<M and farm[nx][ny] == 1:
                q.append((nx, ny))
                farm[nx][ny] = 0

T = int(input())  
for _ in range(T):          
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
        
    for _ in range(K):
        x, y = map(int, input().split())
        x, y = y, x
        farm[x][y] = 1
        
    cnt = 0

    for i in range(M):
        for j in range(N):
            if farm[j][i] == 1:
                bfs(j, i)
                cnt += 1
                
    print(cnt)