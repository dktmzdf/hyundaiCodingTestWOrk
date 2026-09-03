def solution(arr, intervals):
    answer = []
    numArr1 = []
    numArr2 = []

    for num in range(intervals[0][0], intervals[0][1] + 1):
        answer.append(arr[num])

    for num in range(intervals[1][0], intervals[1][1] + 1):
        answer.append(arr[num])

    return answer
