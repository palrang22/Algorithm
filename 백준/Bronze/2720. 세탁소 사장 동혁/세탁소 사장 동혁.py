N = int(input())

for i in range(N):
    C = int(input())
    print(C//25, end=' ')
    print((C := C % 25) // 10, end = ' ')
    print((C := C % 10) // 5, end = ' ')
    print((C := C % 5))