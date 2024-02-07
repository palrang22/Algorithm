import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rel = [tuple(map(int, input().split())) for _ in range(M)]

def fw(N, rel):
    dis = [[float('inf')]*N for _ in range(N)]
    for i in range(N):
        dis[i][i] = 0
    for a, b in rel:
        dis[a-1][b-1] = 1
        dis[b-1][a-1] = 1
        
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    
    kb = [sum(dis[i]) for i in range(N)]
    return (kb.index(min(kb)) + 1)

print(fw(N, rel))