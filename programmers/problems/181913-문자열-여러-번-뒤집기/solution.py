def solution(my_string, queries):
    answer = ""
    originArr = list(my_string)
    reverseStr = []
    # 쿼리를 인덱스 반대로해서 돌리기?
    for query in queries:
        reverseStr.clear()
        for idx in range(query[len(query) - 1], query[0] - 1, -1):
            # print(originArr[idx], end="")
            # print(idx, end="")
            reverseStr.append(originArr[idx])
        # print(reverseStr)
        for i in range(len(reverseStr)):
            originArr[query[0] + i] = reverseStr[i]

        # print(originArr)

    return "".join(originArr)
