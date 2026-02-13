import sys
input = sys.stdin.readline

n = int(input())
queue_or_stack = list(map(int, input().split(" ")))
first_lst = list(map(int, input().split(" ")))
m = int(input())
elements = list(map(int, input().split(" ")))


stack_lst = []

for idx, i in enumerate(queue_or_stack):
    if i == 0:
        stack_lst.append(first_lst[idx])

stack_lst.reverse()

for i in elements:
    stack_lst.append(i)

for i in range(m):
    print(stack_lst[i], end=" ")