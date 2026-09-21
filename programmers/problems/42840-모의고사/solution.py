def solution(answers):
    temp = []
    a1_Count = 0
    a2_Count = 0
    a3_Count = 0

    a1_Array = [1, 2, 3, 4, 5]  #
    a2_Array = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    a3_Array = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10

    for idx in range(len(answers)):
        if a1_Array[idx % 5] == answers[idx]:
            a1_Count += 1
        if a2_Array[idx % 8] == answers[idx]:
            a2_Count += 1
        if a3_Array[idx % 10] == answers[idx]:
            a3_Count += 1

    maxCount = max(a1_Count, a2_Count, a3_Count)

    if maxCount == a1_Count:
        temp.append(1)
    if maxCount == a2_Count:
        temp.append(2)
    if maxCount == a3_Count:
        temp.append(3)
        
    return temp
