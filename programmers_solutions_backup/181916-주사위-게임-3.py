from collections import Counter


def solution(a, b, c, d):
    answer = 0
    numList = [a, b, c, d]
    CounterDic = Counter(numList)
    # print(Test)
    # for aa in Test:
    #     print(aa)
    # print(f"{len(Test)}a")

    # 4
    if len(CounterDic) == 1:
        answer = 1111 * a
    # 3
    if len(CounterDic) == 2:
        if CounterDic[min(numList)] == 3:
            answer = (min(numList) * 10 + max(numList)) ** 2
        elif CounterDic[min(numList)] == 2:
            answer = (min(numList) + max(numList)) * (max(numList) - min(numList))
        else:
            answer = (min(numList) + max(numList) * 10) ** 2
    # 2
    if len(CounterDic) == 3:
        q = 0
        r = 0
        for n in numList:
            if CounterDic[n] == 1:
                if q == 0:
                    q = n
                else:
                    r = n
        answer = q * r

    # 1
    if len(CounterDic) == 4:
        answer = min(numList)

    return answer
