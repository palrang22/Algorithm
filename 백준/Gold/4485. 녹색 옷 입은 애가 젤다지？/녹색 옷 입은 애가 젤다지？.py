from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

result = []
n = int(input())
while n!=0:
    graph  = [[1] for _ in range(n)]
    for idx in range(n):
        graph[idx] = list(map(int, input().split()))
    loss = [[float('inf')]*n for _ in range(n) ]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    mystate = []
    heappush(mystate,(graph[0][0] , [0,0]))
    loss[0][0] = graph[0][0]

    while mystate:
        weight,(x,y) = heappop(mystate)
        if loss[x][y] < weight:
            continue
        
        for idx in range(4):
            xx = x + dx[idx]
            yy = y + dy[idx]
            if (0<=xx<n) and (0<=yy<n):
                cost = weight + graph[xx][yy]
                if loss[xx][yy] > cost:
                    loss[xx][yy] = cost
                    heappush(mystate,(cost , [xx,yy]))
                    
    result.append(loss[-1][-1])
    n = int(input())

for idx in range(len(result)):
    print(f"Problem {idx+1}: {result[idx]}")