def solution(participant, completion):
    parti_dict = dict.fromkeys(participant, 0)
    for i in participant:
        parti_dict[i] += 1
    for j in completion:
        parti_dict[j] -= 1
        
    answer = [k for k, v in parti_dict.items() if v >= 1]
    return answer[0]