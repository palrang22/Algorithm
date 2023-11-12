import sys

class Stack:
    def __init__(self):
        self.listStack = []
    
    def push(self, x): #1
        self.listStack.append(x)
    
    def pop(self): #2
        print(int(self.listStack.pop()) if self.listStack else -1)
        
    def lenStack(self): #3
        print(len(self.listStack))
        
    def printisEmpty(self): #4
       if len(self.listStack) == 0: print(1)
       else: print(0)
    
    def top(self): #5
        print(int(self.listStack[-1]) if self.listStack else -1)

N = int(sys.stdin.readline().strip())
astack = Stack()

for _ in range(N):
    a = sys.stdin.readline().split()
    if len(a) > 1:
        astack.push(a[1])
    if a[0] == '2':
        astack.pop()
    if a[0] == '3':
        astack.lenStack()
    if a[0] == '4':
        astack.printisEmpty()
    if a[0] == '5':
        astack.top()