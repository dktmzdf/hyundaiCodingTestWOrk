def solution(names):
    answer = []
    for idx in range(len(names)):
        if idx % 5 == 0:
            answer.append(names[idx])
    return answer
