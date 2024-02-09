import heapq
import sys

input = sys.stdin.readline

lst = []
heapq.heapify(lst)

N = int(input())
for _ in range(N):
    a = int(input())
    
    if a == 0:
        try:
            b = heapq.heappop(lst)
            print(b)
        except:
            print(0)
    else:
        heapq.heappush(lst,a)
        