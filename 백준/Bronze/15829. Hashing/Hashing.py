alphabet_list = [chr(i) for i in range(97, 123)]
alphabet_dict = {}

for (idx, i) in enumerate(alphabet_list):
    alphabet_dict[i] = idx + 1

N = input() #버림
exponent = 0
result = 0
input_list = list(input())

for i in input_list:
    result += alphabet_dict[i] * 31**exponent
    exponent += 1

print(result%1234567891)