import sys
input = sys.stdin.readline

st = input()
row = int(input())

for _ in range(row):
    word, start, end = input().split()
    start, end = int(start), int(end)
    count = 0

    for i in range(start, end+1):
        if st[i] == word:
            count += 1
    
    print(count)