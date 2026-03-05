import sys
input = sys.stdin.readline


def wave(idx):
        dp = [1, 1, 1, 2, 2]
        for _ in range(idx-5):
            dp.append(0)

        for i in range(5, idx):
            dp[i] = dp[i-1] + dp[i-5]
        
        return dp[idx-1]

n = int(input())

for _ in range(n):
    idx = int(input())
    print(wave(idx))