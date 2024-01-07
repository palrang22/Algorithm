import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

pp = deque([i for i in range(1,N+1)])
seq = []

while len(pp) > 0:

    for _ in range(K-1):
        a = pp.popleft()
        pp.append(a)
    
    b = pp.popleft()
    seq.append(b)


print('<' + ', '.join(map(str, seq)) + '>')