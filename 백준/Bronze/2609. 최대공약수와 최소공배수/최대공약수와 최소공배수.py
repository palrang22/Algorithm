def gcd(a,b):
    x = max([a,b])
    y = min([a,b])

    while True:
        x, y = y, x%y
        if y == 0:
            return x
        
def lcm(c,d):
    lcm = c * d // gcd(c,d)
    return lcm

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))