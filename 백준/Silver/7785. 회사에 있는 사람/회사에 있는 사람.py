import sys
input = sys.stdin.readline

n = int(input())
st = set()

for _ in range(0, n):
    i, j = input().split(" ")
    if j == "enter\n":
        st.add(i)
    if j == "leave\n":
        st.remove(i)

st = sorted(st, reverse=True)
print("\n".join(st))