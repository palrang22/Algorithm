from collections import deque

cptnum = int(input())
relnum = int(input())

rel = {}
visited = [False]*(cptnum+1)

for i in range(1, cptnum+1):
    rel[i] = []

for _ in range(relnum):
    a, b = map(int,input().split())
    rel[a].append(b)
    rel[b].append(a)

def bfs(relation):
    q = deque()
    q.append(1)
    visited[1] = True
    
    while q:
        cur = q.popleft()
        for relcpt in rel[cur]:
            if visited[relcpt] == False:
                q.append(relcpt)
                visited[relcpt] = True

bfs(rel)
print(visited.count(True) - 1)