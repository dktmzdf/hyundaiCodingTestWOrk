def solution(number):
    answer = 0
    sum = 0
    for c in number:
        sum += int(c)

    return sum % 9
