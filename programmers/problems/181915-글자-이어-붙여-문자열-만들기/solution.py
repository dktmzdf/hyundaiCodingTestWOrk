def solution(my_string, index_list):
    answer = []
    for idx in index_list:
        answer.append(my_string[idx])
    return "".join(answer)
