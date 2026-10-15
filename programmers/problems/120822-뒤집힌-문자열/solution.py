def solution(my_string):
    answer = []
    for c in range(len(my_string) - 1, -1, -1):
        answer.append(my_string[c])

    return "".join(answer)
