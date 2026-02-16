import sys
input = sys.stdin.readline

n = int(input())
lst_n = sorted(list(map(int, input().split(" "))))
m = int(input())
lst_m = list(map(int, input().split(" ")))


def binary_search(target):
    left = 0
    right = len(lst_n) - 1

    while left <= right:
        mid = (left+right) // 2
        criteria = lst_n[mid]
        
        if criteria > target:
            right = mid - 1
        elif criteria < target:
            left = mid + 1
        else:
            return 1
    
    return 0

for i in lst_m:
    print(binary_search(i))