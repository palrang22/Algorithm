from heapq import heapify, heappop, heappush
 
N = int(input())
A = []

for _ in range(N):
    card = int(input())
    heappush(A, card)

heapify(A)   
sum = 0

while len(A)>1:
    pop1 = heappop(A)
    pop2 = heappop(A)
    temp = pop1 + pop2
    sum += temp
    heappush(A, temp)
    
print(sum)