from collections import deque
import sys

input = sys.stdin.readline

def findcb(lst,x,y):
    q = deque()
    q.append((x,y))
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    tf[x][y] = True
    
    while q:
        a, b = q.popleft()
        
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            
            if 0 <= nx < N and 0 <= ny < N and lst[nx][ny] == lst[a][b] and tf[nx][ny] == False:
                tf[nx][ny] = True
                q.append((nx,ny))

N = int(input())
nlst = [list(input().strip()) for _ in range(N)]
ylst = []
for i in nlst:
    a = ['R' if j=='G' else j for j in i]
    ylst.append(a)

tf = [[False]*N for _ in range(N)]       
ncount = 0

for i in range(N):
    for j in range(N):
        if not tf[i][j]:
            findcb(nlst, i, j)
            ncount += 1

tf = [[False]*N for _ in range(N)]
ycount = 0

for i in range(N):
    for j in range(N):
        if not tf[i][j]:
            findcb(ylst, i, j)
            ycount += 1
    
print(ncount, ycount, end = ' ')