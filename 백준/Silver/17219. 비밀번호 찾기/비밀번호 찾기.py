N, M = map(int, input().split())
pw_dict = {}

for _ in range(N):
    adr, pw = map(str, input().split())
    pw_dict[adr]  = pw

for _ in range(M):
    search_adr = input()
    print(pw_dict[search_adr])