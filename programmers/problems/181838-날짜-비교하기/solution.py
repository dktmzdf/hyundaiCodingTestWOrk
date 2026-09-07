def solution(date1, date2):
    answer = 0
    for idx in range(3):
        if int(date1[idx]) < int(date2[idx]):
            return 1
        if int(date1[idx]) > int(date2[idx]):
            return 0

    return answer
