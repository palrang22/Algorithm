a, b = map(int, input().split())
c = int(input())
d = int(input())
  
if b <= d * (c-a) and a<=c:
    print(1)

else:
    print(0)
