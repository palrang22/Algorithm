class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque: # 연결리스트 개념으로 구현한 Deque
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def popFirst(self):
        if not self.head:
            return None
        pop_value = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return pop_value.value
    

    
n = int(input())
k = int(input())
apple_set =  set((int(x)-1, int(y)-1) for _ in range(0,k) for (x, y) in [input().split(" ")])
l = int(input())
change_list = [(int(x), y) for _ in range(0,l) for (x, y) in [input().split(" ")]]

def move(old_current: tuple, direction: int) -> tuple:
    ox, oy = old_current[0], old_current[1]
    dx, dy = direction_list[direction][0], direction_list[direction][1]
    return (ox+dx, oy+dy)

def is_apple(current_spot: tuple, apple_set: set) -> bool:
    if current_spot in apple_set:
        return True
    else:
        return False

def new_direction(old_direction: int, changed_tuple: tuple) -> int:
    direction = 1 if changed_tuple[1] == "D" else -1
    return (old_direction + direction) % 4

def is_collide(old_list: set, current: tuple, n: int) -> bool:
    if current in old_list:
        return True
    dx, dy = current[0], current[1]
    if dx == -1 or dy == -1 or dx == n or dy == n:
        return True
    return False
    

time_idx = 0
current_time = 0
current_spot = (0,0)
current_direction = 1
current_body = Deque()
body_set = set()
time_list = [i[0] for i in change_list]
direction_list = [(-1,0), (0,1), (1,0), (0,-1)]

current_body.append((0,0))
body_set.add((0,0))

while True:
    current_time += 1
    current_spot = move(current_spot, current_direction)

    if is_collide(body_set, current_spot, n):
        break

    if is_apple(current_spot, apple_set):
        apple_set.remove(current_spot)
    else:
        first_value = current_body.popFirst()
        body_set.remove(first_value)

    current_body.append(current_spot)
    body_set.add(current_spot)

    if time_idx!= l and current_time == time_list[time_idx]:
        current_direction = new_direction(current_direction, change_list[time_idx])
        time_idx += 1

print(current_time)