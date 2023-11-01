divisor = []

while True:
    N = int(input())
    if N == -1:
        break
    else:
        for i in range(1, N):
            if N % (i) == 0:
                divisor.append(i)
        
        total = sum(divisor)
        
        if N != total:
            print(N,"is NOT perfect.")
        else:
            print(f"{N} = ", end = "")
            for idx, k in enumerate(divisor):
                if idx == (len(divisor)-1):
                    print(k)
                else:
                    print(f"{k} +", end = " ")
    divisor = []