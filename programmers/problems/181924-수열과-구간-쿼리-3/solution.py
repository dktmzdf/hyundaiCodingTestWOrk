def solution(arr, queries):

    for query in queries:
        IndexIValue = arr[query[0]]
        IndexJValue = arr[query[1]]

        arr[query[0]] = IndexJValue
        arr[query[1]] = IndexIValue
        # print(arr)

    return arr
