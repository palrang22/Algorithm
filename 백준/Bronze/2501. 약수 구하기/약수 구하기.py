divisor = []
N, K = map(int, input().split())

for i in range(1, N+1):
    if N % (i) == 0:
        divisor.append(i)
        
try: print(divisor[K-1])
except: print(0)