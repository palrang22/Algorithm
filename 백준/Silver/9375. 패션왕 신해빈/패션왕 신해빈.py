for _ in range(int(input())):
    clothes = int(input())
    fashion = {}
    count = 1
 
    for _ in range(clothes):
        a, b = map(str, input().split())
        if b not in fashion:
            fashion[b] = []
        fashion[b].append(a)
    
    for i in fashion:
        count = count * (len(fashion[i])+1)
    
    print(count-1)