import sys
input = sys.stdin.readline

def main():
    a, b, c = map(int, input().split())

    def pow_mod(a, b, c) -> int:
        if b == 0:
            return 1
        if b == 1:
            return a % c
        
        half = pow_mod(a, b//2, c)

        if b % 2 == 0:
            return half * half % c
        else:
            return (half * half * a) % c
        
    print(pow_mod(a, b, c))
    
main()