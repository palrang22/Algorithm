def solution(n):
    a = 1
    lst = []
    
    while a <= n ** 0.5 :
        if n % a == 0:
            lst.append(a)
            lst.append(n//a)
        a += 1
    
    return sum(set(lst))