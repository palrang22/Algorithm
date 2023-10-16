N = int(input())


for i in range(1, N+1):
    space = " " * (N-i)
    star = "*" * (2*i-1)
    print(space+star)
    
for i in range(N-1, 0, -1):
    space = " " * (N-i)
    star = "*" * (2*i-1)
    print(space+star)