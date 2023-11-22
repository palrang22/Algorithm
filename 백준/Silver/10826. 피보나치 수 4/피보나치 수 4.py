def fib_fast(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for _ in range(n-1):
        c = b
        b = a+b
        a = c
    return b

n = int(input())

print(fib_fast(n))