class MaxHeap:
    def __init__(self):
        self.heap = []

    def head(self):
        if self.count() == 0:
            return None
        return self.heap[0]

    def count(self):
        return len(self.heap)

    # 리프노드 맨 마지막 값으로 삽입
    def append(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap)-1)

    # 가장 위 노드 (최댓값) 삭제
    def pop(self):
        if len(self.heap) == 0 :
            return None
        elif len(self.heap) == 1:
            return_val = self.heap.pop()
        else:
            return_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.sift_down(0)
        return return_val
    
    # 위로 올라가며 비교
    def sift_up(self, idx):
        while idx > 0:
            old_idx = (idx-1) // 2
            if self.heap[idx] > self.heap[old_idx]:
                self.heap[idx], self.heap[old_idx] = self.heap[old_idx], self.heap[idx]
                idx = old_idx
            else:
                break
    
    # 밑으로 내려가며 비교
    def sift_down(self, idx):
        size = len(self.heap)-1
        while True:
            left = idx * 2 + 1
            right = idx * 2 + 2
            parent = idx

            if left <= size and self.heap[left] > self.heap[parent]:
                parent = left
            if right <= size and self.heap[right] > self.heap[parent]:
                parent = right

            if parent == idx:
                break

            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent


class MinHeap:
    def __init__(self):
        self.heap = []

    def head(self):
        if self.count() == 0:
            return None
        return self.heap[0]

    def count(self):
        return len(self.heap)

    # 리프노드 맨 마지막 값으로 삽입
    def append(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap)-1)

    # 가장 위 노드 (최댓값) 삭제
    def pop(self):
        if len(self.heap) == 0 :
            return None
        elif len(self.heap) == 1:
            return_val = self.heap.pop()
        else:
            return_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.sift_down(0)
        return return_val
    
    # 위로 올라가며 비교
    def sift_up(self, idx):
        while idx > 0:
            old_idx = (idx-1) // 2
            if self.heap[idx] < self.heap[old_idx]:
                self.heap[idx], self.heap[old_idx] = self.heap[old_idx], self.heap[idx]
                idx = old_idx
            else:
                break
    
    # 밑으로 내려가며 비교
    def sift_down(self, idx):
        size = len(self.heap)-1
        while True:
            left = idx * 2 + 1
            right = idx * 2 + 2
            parent = idx

            if left <= size and self.heap[left] < self.heap[parent]:
                parent = left
            if right <= size and self.heap[right] < self.heap[parent]:
                parent = right

            if parent == idx:
                break

            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(0, n):
    m = int(input())
    case_lst = []
    small_lst = MaxHeap()
    big_lst = MinHeap()
    return_lst = []
    
    while len(case_lst) < m:
        case_lst.extend(map(int, input().split()))

    for (idx, i) in enumerate(case_lst):
        if small_lst.count() == 0 or i <= small_lst.head():
            small_lst.append(i)
        else:
            big_lst.append(i)

        if small_lst.count() > big_lst.count() + 1:
            big_lst.append(small_lst.pop())
        elif big_lst.count() > small_lst.count():
            small_lst.append(big_lst.pop())

        if idx % 2 == 0:
            return_lst.append(small_lst.head())

    print(len(return_lst))

    for i in range(0, len(return_lst), 10):
        print(" ".join(map(str, return_lst[i:i+10])))
