import sys
input = sys.stdin.readline

n = int(input())
video = [list(map(int, input().rstrip())) for _ in range(n)]
result  = []

def quad(n, video):
    
    count = 0
    for i in video:
        count += sum(i)
    
    if count == n ** 2:
        return "1"
    elif count == 0:
        return "0"
    else:
        half = n // 2
        top_left = [i[:half] for i in video[:half]]
        top_right = [i[half:] for i in video[:half]]
        bot_left = [i[:half] for i in video[half:]]
        bot_right = [i[half:] for i in video[half:]]

        return (
            "("
            + quad(half, top_left)
            + quad(half, top_right)
            + quad(half, bot_left)
            + quad(half, bot_right)
            + ")"
        )

print(quad(n, video))