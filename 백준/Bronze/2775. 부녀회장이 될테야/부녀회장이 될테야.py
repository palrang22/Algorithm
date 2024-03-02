import sys
input = sys.stdin.readline


for _ in range(int(input())):
    k = int(input())
    n = int(input())

    floor = [i for i in range(1, n+1)]

    for _ in range(k):
        for i in range(n):
            if i == 0:
                floor[i] = 1
                continue
            else:
                floor[i] = floor[i]+floor[i-1]

    print(floor[-1])