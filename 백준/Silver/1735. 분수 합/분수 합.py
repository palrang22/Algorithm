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
    return lcm
    
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

deno = lcm(a2, b2)
num = (a1*b2 + b1*a2) // gcd(a2,b2)

if gcd(num, deno) == 1:
    print(num, deno)
else:
    print(num//gcd(num, deno), deno//gcd(num, deno))