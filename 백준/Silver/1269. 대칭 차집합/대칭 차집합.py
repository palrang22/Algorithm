import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lst_a = sorted(list(map(int, input().split(" "))))
lst_b = sorted(list(map(int, input().split(" "))))

pointer_a, pointer_b = 0, 0
common = 0

while pointer_a < n and pointer_b < m:
    if lst_a[pointer_a] < lst_b[pointer_b]:
        pointer_a += 1
    elif lst_a[pointer_a] == lst_b[pointer_b]:
        common += 1
        pointer_a += 1
    else:
        pointer_b += 1

print(n + m - 2*common)