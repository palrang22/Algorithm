import sys
input = sys.stdin.readline


def feb_dp(n):
    feb_lst = [None for _ in range(0, n)]
    feb_lst[0] = 1
    feb_lst[1] = 1
    count = 0

    for i in range(2, n):
        count += 1
        feb_lst[i] = feb_lst[i-1] + feb_lst[i-2]
    return feb_lst[n-1], count

n = int(input())

feb_recursion_count = feb_dp(n)[0]
feb_dp_count = feb_dp(n)[1]

print(feb_recursion_count, feb_dp_count)