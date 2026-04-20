def solution(progresses, speeds):
    count = len(progresses)
    lst = []
    for i in range(count):
        days = 0
        done = progresses[i]
        speed = speeds[i]
        
        while done < 100:
            days += 1
            done += speed
            
        lst.append(days)
        
    current = lst[0]
    distribute = 1
    answer = []
    
    for i in range(1, len(lst)):
        if current < lst[i]:
            answer.append(distribute)
            distribute = 1
            current = lst[i]
        else:
            distribute += 1
            
    answer.append(distribute)
            
    return answer