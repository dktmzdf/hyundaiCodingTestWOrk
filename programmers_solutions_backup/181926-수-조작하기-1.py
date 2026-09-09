def solution(n, control):
    answer = 0
    #     "w" : n이 1 커집니다.
    # "s" : n이 1 작아집니다.
    # "d" : n이 10 커집니다.
    # "a" : n이 10 작아집니다.
    for i in range(len(control)):
        if control[i] == "w":
            n += 1
        elif control[i] == "s":
            n -= 1
        elif control[i] == "d":
            n += 10
        elif control[i] == "a":
            n -= 10
    
    return n