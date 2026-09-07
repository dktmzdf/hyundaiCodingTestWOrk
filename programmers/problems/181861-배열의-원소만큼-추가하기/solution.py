def solution(arr):
    answer = []
    for num in arr:
        for a in range(num):
            answer.append(num)
    return answer
