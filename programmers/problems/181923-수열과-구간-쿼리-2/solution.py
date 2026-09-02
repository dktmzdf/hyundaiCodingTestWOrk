def solution(arr, queries):
    answer = []
    for query in queries:
        i, j, k = query
        selectValue = int(1e9)
        for idx in range(i, j + 1):
            if arr[idx] > k and arr[idx] < selectValue:
                selectValue = arr[idx]

        sum = selectValue if selectValue != int(1e9) else -1

        answer.append(sum)
    return answer
