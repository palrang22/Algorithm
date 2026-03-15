import sys
input = sys.stdin.readline

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
    if a[0] == "push":
        astack.push(a[1])
    elif a[0] == "pop":
        astack.pop()
    elif a[0] == "size":
        astack.lenStack()
    elif a[0] == "empty":
        astack.printisEmpty()
    elif a[0] == "top":
        astack.top()