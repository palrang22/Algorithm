import sys
input = sys.stdin.readline

word_dict = {}

n, m = map(int, input().split())

for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1

word_lst = sorted(word_dict.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))
for word, count in word_lst: print(word)