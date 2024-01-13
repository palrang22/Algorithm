import sys

N, r, c = map(int, input().split())

def findZ(N, r, c, cnt):
    len = 2 ** N
    half = len // 2
    
    if N == 1:
        if r == 1 and c == 1:
            cnt += 3
        elif r == 1:
            cnt += 2
        elif c == 1:
            cnt += 1
            
        print(cnt)
        return
        
    
    if r>=half and c>=half:
        findZ(N-1, r-half, c-half, cnt + half*half*3)
        
    elif r>=half :
        findZ(N-1, r-half, c, cnt + half*half*2)
        
    elif c>=half:
        findZ(N-1, r, c-half, cnt + half*half)
        
    else:
        findZ(N-1, r, c, cnt)
        
findZ(N, r, c, 0)