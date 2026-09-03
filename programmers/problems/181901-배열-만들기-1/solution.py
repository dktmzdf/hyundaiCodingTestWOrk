def solution(n, k):
    answer = []
    AscNum = 1

    while k * AscNum <= n:
        answer.append(k * AscNum)
        AscNum += 1

    return answer
