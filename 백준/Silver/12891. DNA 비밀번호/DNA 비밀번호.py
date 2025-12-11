arr_len, target_len = map(int, input().split(" "))
arr = input()
min_count = list(map(int, input().split()))


dna_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

first = 0
last = target_len
count = 0

current_count = [0, 0, 0, 0]

for i in arr[first:last]:
    current_count[dna_dict[i]] += 1


def check_if_valid(current_count, min_count):
    for i in range(0, 4):
        if current_count[i] < min_count[i]:
            return False
    return True


while last <= arr_len:
    if check_if_valid(current_count, min_count):
        count += 1

    if last == arr_len:
        break

    current_count[dna_dict[arr[first]]] -= 1
    current_count[dna_dict[arr[last]]] += 1

    first += 1
    last += 1

    
print(count)