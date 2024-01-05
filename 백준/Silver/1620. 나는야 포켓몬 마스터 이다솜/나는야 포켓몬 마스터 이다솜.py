import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
pokedex = {}

for i in range(1, N+1):
    pokeName = input().rstrip()
    pokedex[i] = pokeName
    
reverseDex = {v: k for k, v in pokedex.items()}

for _ in range(Q):
    question = input().rstrip()
    try:
        question = int(question)
        print(pokedex[question])
    except:
        print(reverseDex[question])