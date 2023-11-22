f = []

def fib_fast(n):
    f.insert(0,0)
    f.insert(1,1)
    for i in range(2,n+1):
        a = f[i-1] + f[i-2]
        f.insert(i,a)
        
n = int(input())

fib_fast(n)
print(f[n])