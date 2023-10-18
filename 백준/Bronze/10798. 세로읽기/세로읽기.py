square = []

for i in range(5):
    hang = str(input())
    square.append(hang)
    

for i in range(15):
    for j in range(5):
        try:
            print(square[j][i], end = '')
        
        except:
            continue