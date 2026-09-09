def solution(my_string, indices):
    answer = []
    for idx in range(len(my_string)):
        if indices.count(idx) == 0:
            answer.append(my_string[idx])

    return "".join(answer)
