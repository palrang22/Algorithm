while True:
    N = int(input())
    if N == -1:
        break
    
    divisor = [i for i in range(1, N) if N % i == 0]
    # List Comprehension 사용해 한줄로 리스트 생성
    total = sum(divisor)

    if N != total:
        print(f"{N} is NOT perfect.")
    else:
        divisors_str = " + ".join(map(str, divisor))
        # map을 이용해 List 값들을 str 로 받고, join 이용해 사이사이에 "+" 넣기
        print(f"{N} = {divisors_str}")
                
    ## 초기화 구문 삭제