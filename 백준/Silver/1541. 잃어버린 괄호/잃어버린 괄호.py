exp = list(map(str, input().split('-')))
new = []

for i in exp:
    a = list(map(int, i.lstrip('0').split('+')))
    new.append(a)

newSum = sum(new[0])

for j in new[1:]:
    newSum -= sum(j)

print(newSum)