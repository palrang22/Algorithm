import sys
input = sys.stdin.readline

n = int(input())
num_lst = list(map(int, input().split(" ")))
op_lst = list(map(int, input().split(" ")))

def backtracking(idx: int, op_lst: list, cur: int):
    if idx == n:
        return cur, cur
    
    max_val = None
    min_val = None
    
    for i in range(4):
        if op_lst[i] > 0:
            op_lst[i] -= 1
            
            if i == 0:
                nex = cur + num_lst[idx]
            elif i == 1:
                nex = cur - num_lst[idx]
            elif i == 2:
                nex = cur * num_lst[idx]
            else:
                if cur < 0:
                    nex = - (-cur // num_lst[idx])
                else:
                    nex = cur // num_lst[idx]

            child_max, child_min = backtracking(idx+1, op_lst, nex)

            if max_val is None:
                max_val = child_max
                min_val = child_min
            else:
                max_val = max(max_val, child_max)
                min_val = min(min_val, child_min)

            op_lst[i] += 1

    return max_val, min_val


max_val, min_val = backtracking(1, op_lst, num_lst[0])
print(max_val, min_val)