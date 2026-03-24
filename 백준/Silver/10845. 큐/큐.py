import sys
from collections import deque

class Queue(deque):
    def push(self, x):
        self.append(x)

    def pop(self):
        print(int(super().popleft()) if self else -1)

    def size(self):
        print(len(self))

    def empty(self):
        print(0 if self else 1)

    def front(self):
        print(self[0] if self else -1)

    def back(self):
        print(self[-1] if self else -1)

N = int(sys.stdin.readline().strip())
aqueue = Queue()

for _ in range(N):
    a = sys.stdin.readline().split()
    if len(a) > 1:
        aqueue.push(a[1])
    if a[0] == 'pop':
        aqueue.pop()
    if a[0] == 'size':
        aqueue.size()
    if a[0] == 'empty':
        aqueue.empty()
    if a[0] == 'front':
        aqueue.front()
    if a[0] == 'back':
        aqueue.back()
