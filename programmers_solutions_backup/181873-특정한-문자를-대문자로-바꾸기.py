def solution(my_string, alp):
    answer = list(my_string.lower())
    for idx in range(len(answer)):
        if answer[idx] == alp:
            answer[idx] = alp.upper()
    return "".join(answer)
