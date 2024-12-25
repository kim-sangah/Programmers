def solution(numLog):
    answer = ''
    num_dict = {1:"w", -1:"s", 10:"d", -10:"a"}
    for i in range(len(numLog)-1):
        answer += num_dict[numLog[i+1] - numLog[i]]
    return answer