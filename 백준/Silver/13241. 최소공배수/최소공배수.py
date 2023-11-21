def gcd(a,b):
    x = max([a,b])
    y = min([a,b])

    while True:
        z = y
        y = x%y
        x = z
        if y == 0:
            return z
        
def lcm(c,d):
    lcm = c * d // gcd(c,d)
    print(lcm)
    return lcm
    
    
a, b = map(int, input().split())
lcm(a,b)