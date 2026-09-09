def solution(my_string):
    answer = []
    arr = list(my_string)
    for idx in range(len(arr)):
        answer.append(my_string[idx : len(my_string)])

    answer.sort()
    return answer
