def solution(arr, idx):
    answer = -1
    for arrIndex in range(idx, len(arr)):
        if arr[arrIndex] == 1:
            answer = arrIndex
            break
    return answer
