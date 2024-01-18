for i in range(int(input())):
    num = int(input())
    dp = [0] * (num)
    
    if num == 1: print(1)
    elif num == 2: print(2)
    elif num == 3: print(4)
    else:

        dp[0] = 1 #1: 1
        dp[1] = 2 #2: 11 / 02
        dp[2] = 4 #3 : 111 / 21 / 12 / 30

        for j in range(3, num):
            dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
            
        print(dp[num-1])