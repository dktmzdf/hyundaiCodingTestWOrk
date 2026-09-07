def solution(arr, queries):
    answer = []
    for query in queries:
        for idx in range(query[0], query[1] + 1):
            arr[idx] += 1
    return arr
