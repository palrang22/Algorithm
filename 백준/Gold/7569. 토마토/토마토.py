import sys
from collections import deque
input = sys.stdin.readline

def bfs(lst, tmtlst, x, y, z):
    q = deque()
    for i in tmtlst:
        q.append(i)
    
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    maxcnt = 0
    
    while q:
        x, y, z, cnt = q.popleft()
        maxcnt = max(cnt,maxcnt)
        
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            
            if 0<= nx < M and 0 <= ny < N and 0<= nz < H and lst[nz][ny][nx] == 0:
                lst[nz][ny][nx] = 1
                q.append((nx,ny,nz,cnt+1))
                
    for i in lst:
        for j in i:
            if 0 in j:
                return -1
    
    return maxcnt

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tmtlst = []
count = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
               tmtlst.append((k,j,i,0))
               
minday = bfs(box, tmtlst, M, N, H)

print(minday)