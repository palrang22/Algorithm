import sys
input = sys.stdin.readline

def main():
    n = int(input())
    time = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x: (x[1], x[0]))

    finish = 0
    timetable = []

    for i in time:
        next_st = i[0]
        next_fin = i[1]

        if next_st < finish:
            continue
        else:
            timetable.append(i)
            finish = next_fin

    print(len(timetable))


main()