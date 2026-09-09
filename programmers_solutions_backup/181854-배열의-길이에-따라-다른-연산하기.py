def solution(arr, n):
    answer = arr
    if len(arr) % 2 == 0:
        for idx in range(1, len(arr), 2):
            answer[idx] += n
    else:
        for idx in range(0, len(arr), 2):
            answer[idx] += n
    return answer
