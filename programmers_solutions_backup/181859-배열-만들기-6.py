def solution(arr):
    answer = []
    arrIndex = 0

    while arrIndex < len(arr):
        # print(answer)
        if len(answer) == 0:
            answer.append(arr[arrIndex])
            arrIndex += 1
        elif answer[len(answer) - 1] == arr[arrIndex]:
            answer.pop()
            arrIndex += 1
        elif answer[len(answer) - 1] != arr[arrIndex]:
            answer.append(arr[arrIndex])
            arrIndex += 1

    if len(answer) == 0:
        return [-1]

    return answer
