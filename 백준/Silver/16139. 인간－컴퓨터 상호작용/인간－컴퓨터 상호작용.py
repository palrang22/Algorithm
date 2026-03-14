import sys
input = sys.stdin.readline

st = input().rstrip()
lenst = len(st)
row = int(input())
alphabet_lst = [[0] * (lenst+1) for _ in range(26)]

for idx, i in enumerate(st):
    for j in range(26):
        alphabet_lst[j][idx+1] = alphabet_lst[j][idx]
    alp_idx = ord(i)-97
    alphabet_lst[alp_idx][idx+1] += 1

for _ in range(row):
    word, start, end = input().split()
    word, start, end = word.rstrip(), int(start), int(end)

    alp_idx = ord(word)-97
    print(alphabet_lst[alp_idx][end+1] - alphabet_lst[alp_idx][start])