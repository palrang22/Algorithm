import sys
input = sys.stdin.readline

k, n = map(int, input().split(" "))
lst = [int(input()) for _ in range(k)]

def binary_search():
    left = 1
    right = max(lst)
    length = 0

    while left <= right:
        mid = (right+left) // 2
        if n <= count_cable(mid):
            left = mid + 1
            length = mid
        else:
            right = mid - 1
    return length
        

def count_cable(mid: int):
    cnt = 0
    for i in lst:
        cnt += i // mid
    return cnt

print(binary_search())