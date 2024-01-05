##14890

import sys
input = sys.stdin.readline


def availSlope(roadList, N, L) :
    checkList = [ 0 for i in range(N)]
    
    count = 1 
    
    for i in range(1, N):
                  
        slope = roadList[i] - roadList[i-1]
        
        if slope == 0:
            count += 1
        elif slope == 1 and count >= L:
            count = 1
        elif slope == -1 and count >= 0:
            count = 1 - L
        else: return False
        
    if count >= 0:
        checkList[i] = 1
        
    return sum(checkList)


N, L = map(int, input().split())
count = 0

road = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    count += availSlope(road[i], N, L)\

for j in range(N):
    count += availSlope([road[i][j] for i in range(N)], N, L)
    
print(count)