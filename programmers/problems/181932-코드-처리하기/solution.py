def solution(code):
    if(code==""):
        return "EMPTY"
    mode=0
    answerStr = []
    for idx in range(0, len(code)):
        if code[idx] == '1':
            mode =  1 ^ mode
        else:
            if mode == 0 and idx % 2 == 0:
                answerStr.append(code[idx])
            elif mode == 1 and idx % 2 == 1:
                answerStr.append(code[idx])

    if(answerStr==[]):
            return "EMPTY"

    return ''.join(answerStr)
