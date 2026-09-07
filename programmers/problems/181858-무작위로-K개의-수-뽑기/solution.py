def solution(arr, k):
    answer = []
    tempArr = arr
    # tempArr.sort()

    for num in tempArr:
        if num not in answer:
            answer.append(num)

    for i in range(len(answer), k):
        answer.append(-1)

    return answer[:k]
