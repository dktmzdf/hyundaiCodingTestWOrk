def solution(num_list, n):
    answer = []
    for idx in range(len(num_list)):
        if idx % n == 0:
            answer.append(num_list[idx])
    return answer
