def solution(a, b):
    a_odd = a % 2 == 1
    b_odd = b % 2 == 1

    if a_odd and b_odd:
        answer = a**2 + b**2
    elif a_odd or b_odd:
        answer = 2 * (a + b)
    else:
        answer = abs(a - b)
    return answer
