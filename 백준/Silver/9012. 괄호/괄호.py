import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    braket = list(input().rstrip())
    braStack = []
    
    try:
        for i in braket:
            braStack.append(1) if i == '(' else braStack.pop()
               
        print("YES" if sum(braStack) == 0 else "NO") 

    except:
        print("NO")