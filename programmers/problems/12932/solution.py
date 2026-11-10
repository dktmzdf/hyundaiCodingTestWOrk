def solution(n):
    answer = []
    str_num = str(n)
    for si in range(len(str_num) - 1, -1, -1):
        answer.append(int(str_num[si]))
    return answer
