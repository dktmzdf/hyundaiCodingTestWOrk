def solution(orders):
    answer = 0
    # ice hot 날리고 종류가 뭔지만 알아보자

    dictCount = {}

    for order in orders:
        temp = order.replace("hot", "")
        temp = temp.replace("ice", "")
        # print(temp)
        if temp in dictCount:
            dictCount[temp] += 1
        else:
            dictCount[temp] = 1

    if dictCount.get("americano", -1) != -1:
        answer += dictCount.get("americano", -1) * 4500
    if dictCount.get("anything", -1) != -1:
        answer += dictCount.get("anything", -1) * 4500
    if dictCount.get("cafelatte", -1) != -1:
        answer += dictCount.get("cafelatte", -1) * 5000

    return answer
