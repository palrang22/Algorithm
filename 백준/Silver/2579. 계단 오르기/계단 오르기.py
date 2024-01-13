N = int(input())
scores = [int(input()) for _ in range(N)]

dp = [0] * (N)

if N <= 2:
    print(sum(scores))
    
else:
    dp[0] = scores[0]
    dp[1] = scores[0]+scores[1]

    for i in range(2, N):
        dp[i] = max(scores[i]+scores[i-1]+dp[i-3], scores[i]+dp[i-2])
        

    print(dp[N-1])