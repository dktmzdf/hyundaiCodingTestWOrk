def solution(phone_book):
    answer = True

    # 접두어의 크기를 구한후 크기보다 작은놈은 무시해 버리고 크거나 같은놈만 계산하기.
    checkDic = {}
    sortedArray = sorted(phone_book)
    # sortedArray = phone_book

    # 정렬 하면 비슷놈끼리 있을테니 계산
    for i in range(0, len(sortedArray) - 1):
        if sortedArray[i + 1].startswith(sortedArray[i]):
            return False

        # checkDic[sortedArray[i]] = 1

        # for key, value in checkDic.items():
        #     if len(key) == len(sortedArray[i]):
        #         continue
        #     if checkDic.get(sortedArray[i][0 : len(key)], -1) != -1:
        #         return False

    return answer
