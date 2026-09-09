def solution(a, d, included):
    answer = 0;
    sequence = a;
    for i in range(len(included)):
        if included[i]:
            answer += sequence
            
        sequence += d
    return answer
