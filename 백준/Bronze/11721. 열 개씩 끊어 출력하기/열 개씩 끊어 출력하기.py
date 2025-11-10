word = input()
slice_first = 0
slice_last = 10
count = 1

if len(word) > 10:
    while slice_last < len(word):
        print(word[slice_first:slice_last])
        slice_first += 10
        slice_last += 10
        count += 0
    print(word[slice_first:slice_first + len(word)-10*count])
else:
    print(word)