def cut(x, y, size):

    target = paper[x][y]
    same = True

    if size == 1:
        count[target] += 1
        return
    
    for i in range(0, size):
        for j in range(0, size):
            if paper[x+i][y+j] != target:
                same = False
                break
        if not same:
            break

    if same:
        count[target] += 1
        return
    
    size = size // 3

    for i in range(0, 3):
        for j in range(0, 3):
            cut(x+i*size, y+j*size, size)
    
    

size = int(input())
paper = [list(map(int, input().split(" "))) for _ in range(0, size)]
count = [0, 0, 0]

cut(0, 0, size)
print(count[-1])
print(count[0])
print(count[1])