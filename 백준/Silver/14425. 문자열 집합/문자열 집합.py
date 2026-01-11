lst = list(map(int, input().split(" ")))
n, m = lst[0], lst[1]

target_lst = [input() for _ in range(0,n)]
target_count = 0

for _ in range(0, m):
    if input() in target_lst:
        target_count += 1

print(target_count)