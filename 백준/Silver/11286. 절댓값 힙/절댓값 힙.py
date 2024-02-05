import sys
import heapq

input = sys.stdin.readline
hq = []
heapq.heapify(hq)

for _ in range(int(input())):
    n = int(input())
    
    if n == 0:
        try:
            _, popNum = heapq.heappop(hq)
            print(popNum)
        except:
            print(0)
        
    else:
        heapq.heappush(hq, (abs(n), n))