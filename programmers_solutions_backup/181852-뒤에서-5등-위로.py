def solution(num_list):
    answer = []
    answer.extend(sorted(num_list))

    return answer[5 : len(num_list)]
