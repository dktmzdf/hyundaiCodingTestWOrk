def solution(s):
    answer = True
    stackList = []

    for ss in s:
        if ss == ")":
            if len(stackList) == 0:
                return False
            else:
                stackList.pop()
        elif ss == "(":
            stackList.append(0)

    if len(stackList) != 0:
        return False
    return True
