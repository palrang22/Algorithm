class KeyLogDecoder:
    def __init__(self):
        self.left_stack = []
        self.right_stack = []

    def insert(self, word):
        self.left_stack.append(word)

    def go_left(self):
        if len(self.left_stack) == 0:
            return
        pop = self.left_stack.pop()
        self.right_stack.append(pop)

    def go_right(self):
        if len(self.right_stack) == 0:
            return
        pop = self.right_stack.pop()
        self.left_stack.append(pop)

    def delete(self):
        if len(self.left_stack) == 0:
            return
        self.left_stack.pop()

    def change_into_string(self):
        return "".join(self.left_stack)
    
    def change_into_reversed_string(self):
        return "".join(reversed(self.right_stack))
        
    def process(self, test_case):
        for i in test_case:
            match i:
                case "<":
                    self.go_left()
                case ">":
                    self.go_right()
                case "-":
                    self.delete()
                case _:
                    self.insert(i)
        
        return self.change_into_string() + self.change_into_reversed_string()

n = int(input())
test_case = [input() for _ in range(0,n)]

for i in test_case:
    keylog_decoder = KeyLogDecoder()
    print(keylog_decoder.process(i))