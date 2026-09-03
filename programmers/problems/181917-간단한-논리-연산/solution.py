def solution(x1, x2, x3, x4):
    answer = True

    union1 = x1 or x2
    union2 = x3 or x4
    answer = union1 and union2

    return answer
