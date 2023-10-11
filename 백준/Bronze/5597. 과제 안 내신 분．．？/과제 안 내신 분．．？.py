stdnum = []

for i in range(30):
    stdnum.append(i+1)

for j in range(28):
    oknum = int(input())
    stdnum.remove(oknum)
    
print(min(stdnum))
print(max(stdnum))