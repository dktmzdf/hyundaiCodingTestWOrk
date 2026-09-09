def solution(strArr):
    answer = []
    for test in strArr:
        if "ad" not in test:
            answer.append(test)
    return answer
