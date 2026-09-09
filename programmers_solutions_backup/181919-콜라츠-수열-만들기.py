def solution(n):
    answer = []

    cal = n
    answer.append(n)
    while cal != 1:
        if cal % 2 == 0:
            cal /= 2
        else:
            cal = cal * 3 + 1
        answer.append(cal)

    return answer
