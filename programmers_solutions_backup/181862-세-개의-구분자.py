def solution(myStr):
    answer = []

    makeStr = ""
    for myChr in myStr:
        if myChr == "a" or myChr == "b" or myChr == "c":
            if len(makeStr) != 0:
                answer.append(makeStr)
            makeStr = ""
        else:
            makeStr += myChr

    if len(makeStr) != 0:
        answer.append(makeStr)
    elif len(answer) == 0:
        answer.append("EMPTY")

    return answer
