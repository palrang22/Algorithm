import sys
input = sys.stdin.readline

n = int(input())
talk_lst = set()
cnt = 0

for _ in range(n):
    i = input().rstrip()
    if i == "ENTER":
        cnt += len(talk_lst)
        talk_lst = set()
        continue
    else:
        talk_lst.add(i)

cnt += len(talk_lst)
    

print(cnt)