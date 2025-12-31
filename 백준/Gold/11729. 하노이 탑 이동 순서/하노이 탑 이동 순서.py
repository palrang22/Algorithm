def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    
    aux = 6-start-end
    hanoi(n-1, start, aux)
    print(start, end)
    hanoi(n-1, aux, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)