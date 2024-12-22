N = int(input())
applicant_size = list(map(int, input().split()))
T, P = map(int, input().split())

count = 0

for i in applicant_size:
    if i % T == 0:
        count += i//T
    else:
        count += (i//T + 1)

print(count)
print(N//P, N%P)