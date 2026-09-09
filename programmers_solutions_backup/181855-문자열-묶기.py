def solution(strArr):
    answer = 0
    dic = {}

    for strI in strArr:
        if len(strI) in dic:
            dic[len(strI)].append(strI)
        else:
            dic[len(strI)] = [strI]

    answer = 0
    for key, value in dic.items():
        if len(value) > answer:
            answer = len(value)

    return answer
