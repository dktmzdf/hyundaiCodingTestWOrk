def solution(numLog):
    answer = []
    # "w" : 수에 1을 더한다.
    # "s" : 수에 1을 뺀다.
    # "d" : 수에 10을 더한다.
    # "a" : 수에 10을 뺀다.
    controlValue = 0
    for i in range(1, len(numLog)):
        controlValue = numLog[i] - numLog[i - 1]
        if controlValue == 1:
            answer.append("w")
        elif controlValue == -1:
            answer.append("s")
        elif controlValue == 10:
            answer.append("d")
        elif controlValue == -10:
            answer.append("a")
    return ''.join(answer)
