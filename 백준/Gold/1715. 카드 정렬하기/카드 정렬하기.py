from queue import PriorityQueue
 
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    card = int(input())
    pq.put(card)
    
data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1 :
    get1 = pq.get()
    get2 = pq.get()
    
    temp = get1 + get2
    sum += temp
    pq.put(temp)
    
print(sum)