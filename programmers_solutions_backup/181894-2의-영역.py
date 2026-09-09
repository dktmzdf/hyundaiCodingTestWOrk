def solution(arr):
    answer = []
    startIndex = -1
    endIndex = -1

    for idx in range(len(arr)):
        if arr[idx] == 2:
            if startIndex == -1:
                startIndex = idx
            endIndex = idx

    if startIndex == -1:
        return [-1]
    elif startIndex == endIndex:
        return [arr[startIndex]]

    return arr[startIndex : endIndex + 1]
