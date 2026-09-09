def solution(a, b):
    # 일의 자리씩 더한다 10이 넘기면 step으로 넘기기
    answer = ""
    longNum = ""
    shortNum = ""
    shortLen = 0
    longLen = 0
    if len(a) >= len(b):
        longNum = a
        shortNum = b
        longLen = len(a)
        shortLen = len(b)

    else:
        longNum = b
        shortNum = a
        longLen = len(b)
        shortLen = len(a)

    step = False
    # 있는 자리수까지 더함
    for idx in range(longLen):
        addNum = 0
        if idx < shortLen:
            addNum = int(shortNum[shortLen - idx - 1])

        if step == True:
            addNum += 1
            step = False

        temp = int(longNum[longLen - idx - 1]) + addNum

        if temp >= 10:
            temp = temp % 10
            step = True

        answer += str(temp)

    if step == True:
        answer += "1"

    return "".join(reversed(answer))
