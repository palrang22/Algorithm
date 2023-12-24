import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.listStack = []
    
    def push(self, x):
        self.listStack.append(x)
    
    def pop(self):
        self.listStack.pop() if self.listStack else print("끝")
        
    def printStack(self):
        print(self.listStack)
        
    def sumStack(self):
        print(sum(self.listStack))

N = int(input())
astack = Stack()

for _ in range(N):
    a = int(input())
    if a == 0:
        astack.pop()
    else:
        astack.push(a)
        
astack.sumStack()