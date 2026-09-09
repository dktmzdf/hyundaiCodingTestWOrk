def solution(arr):
    answer = []
    answer.extend(arr)

    if len(arr) & (len(arr) - 1) == 0:
        return answer

    shift = 0
    arrLen = len(arr)

    while True:
        arrLen = arrLen >> 1
        shift += 1
        if arrLen % 2 == 0 and arrLen == 0:
            break

    print(shift)
    answer.extend([0] * (2**shift - len(arr)))

    return answer
