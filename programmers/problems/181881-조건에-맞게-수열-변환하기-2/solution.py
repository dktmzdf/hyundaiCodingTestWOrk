def solution(arr):
    answer = 0
    CalcArr = []
    CalcArr.extend(arr)
    tempArr = []
    repeat = 1
    while True:
        for num in CalcArr:
            if num >= 50 and num % 2 == 0:
                tempArr.append(int(num / 2))
            elif num < 50 and num % 2 == 1:
                tempArr.append(num * 2 + 1)
            else:
                tempArr.append(num)

        if CalcArr == tempArr:
            return repeat - 1

        CalcArr.clear()
        CalcArr.extend(tempArr)
        tempArr.clear()
        repeat += 1
