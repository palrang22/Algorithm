import sys
input = sys.stdin.readline

def main():
    n = int(input())
    distance = list(map(int, input().split()))
    price = list(map(int, input().split()))

    pre_sum = [0] * n
    for i in range(1, n):
        pre_sum[i] = pre_sum[i-1] + distance[i-1]
    
    next_cheap = [-1] * n
    stack = []
    for i in range(n):
        while stack and price[stack[-1]] > price[i]:
            next_cheap[stack.pop()] = i
        stack.append(i)

    fuel = 0
    cost = 0

    for i in range(n-1):
        nc = next_cheap[i]

        if nc == -1:
            need = pre_sum[n-1] - pre_sum[i]
        else:
            need = pre_sum[nc] - pre_sum[i]

        if fuel < need:
            cost += (need-fuel) * price[i]
            fuel = need
        
        fuel -= distance[i]

    print(cost)

main()