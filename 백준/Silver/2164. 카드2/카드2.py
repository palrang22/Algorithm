from collections import deque
import sys

input = sys.stdin.readline

card = deque()

N = int(input())
[card.append(i) for i in range(1,N+1)]

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(*card)