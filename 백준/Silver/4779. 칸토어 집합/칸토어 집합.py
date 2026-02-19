import sys
input = sys.stdin.readline

def cut(step):
    if step == 0:
        return "-"
    line = cut(step-1)
    return line + " "*len(line) + line

while True:
    ipt = input()
    if not ipt:
        break
    step = int(ipt)
    print(cut(step))