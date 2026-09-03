def solution(my_strings, parts):
    answer = []
    for idx in range(len(my_strings)):
        for strIdx in range(parts[idx][0], parts[idx][1] + 1):
            answer.append(my_strings[idx][strIdx])

    return "".join(answer)
