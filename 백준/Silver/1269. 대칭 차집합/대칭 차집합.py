import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
lst_a = set(map(int, input().split(" ")))
lst_b = set(map(int, input().split(" ")))

print(len(lst_a^lst_b))