len_list = int(input())
num_list = list(map(int, input().split(" ")))
sorted_list = sorted(num_list)
target_num = int(input())

pointer_start = 0
pointer_end = len_list - 1

target_count = 0

while pointer_start != pointer_end :
    current_sum = sorted_list[pointer_start] + sorted_list[pointer_end]
    
    if current_sum == target_num:
        target_count += 1
        pointer_start += 1
    elif current_sum < target_num:
        pointer_start += 1
    else:
        pointer_end -= 1

print(target_count)