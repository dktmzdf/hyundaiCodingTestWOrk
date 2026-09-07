def solution(arr, flag):
    answer = []
    tempArr = []
    for idx in range(len(arr)):
        if flag[idx] is True:
            for n in range(arr[idx] * 2):
                answer.append(arr[idx])
        else:
            for n in range(arr[idx]):
                answer.pop()

    return answer
