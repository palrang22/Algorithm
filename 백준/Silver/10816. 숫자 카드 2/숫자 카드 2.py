import sys
input = sys.stdin.readline

n = int(input())
my_lst = sorted(list(map(int, input().split(" "))))
m = int(input())
target_lst = list(map(int, input().split(" ")))

def upper_bound(my_lst, target):
    left = 0
    right = len(my_lst)

    while left < right:
        mid = (left+right) // 2
        if my_lst[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def lower_bound(my_lst, target):
    left = 0
    right = len(my_lst)

    while left < right:
        mid = (left+right) // 2
        if my_lst[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

result = []

for i in target_lst:
    ub = upper_bound(my_lst, i)
    lb = lower_bound(my_lst, i)
    result.append(ub-lb)

print(*result)