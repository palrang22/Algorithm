import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

def countPaper(N, paper):
    
    global blueCnt, whiteCnt
    
    qut = N//2
    
    paperSum = 0
    for i in range(N):
        paperSum += sum(paper[i])
    
    if paperSum == N**2:
        blueCnt += 1
    elif paperSum == 0:
        whiteCnt += 1
    else:
        countPaper(N//2, [row[:qut] for row in paper[:qut]])
        countPaper(N//2, [row[qut:] for row in paper[:qut]])
        countPaper(N//2, [row[qut:] for row in paper[qut:]])
        countPaper(N//2, [row[:qut] for row in paper[qut:]])

blueCnt, whiteCnt = 0, 0
countPaper(N, paper)

print(whiteCnt,blueCnt,end='\n')