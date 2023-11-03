while True:
    a = list(map(int, input().split()))
    
    if sum(a) == 0:
        break
    
    elif max(a)*2 >= sum(a):
        print("Invalid")
        
    elif sum(a) != 0:
        match len(set(a)):
            case 1: print("Equilateral")
            case 2: print("Isosceles")
            case 3: print("Scalene")