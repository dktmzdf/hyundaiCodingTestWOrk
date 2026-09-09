def solution(arr, delete_list):
    answerRemove = []
    answerArr = arr.copy()

    for removeNum in delete_list:
        for arrNum in arr:
            if removeNum == arrNum:
                answerRemove.append(arrNum)

    for num in answerRemove:
        answerArr.remove(num)

    return answerArr
