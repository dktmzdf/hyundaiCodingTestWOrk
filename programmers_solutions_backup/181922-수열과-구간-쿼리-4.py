def solution(arr, queries):
    for query in queries:
        i, j, k = query
        for idx in range(i, j + 1):
            if idx % k == 0:
                arr[idx] += 1
    return arr
