def solution(priorities, location):
    answer = 0

    goalNumber = priorities[location]
    # 순회하면서 인덱스
    arrIndex = 0

    for n in range(9, 0, -1):
        tempArr = []
        temparrIndex = 0
        # 인덱스 넣기 일단 목표 우선순위가 어디서부터 시작해야하는시 계산해야하기 떄문에 순회
        for seq in range(0, len(priorities)):
            if priorities[(arrIndex + seq) % len(priorities)] == n:
                tempArr.append((arrIndex + seq) % len(priorities))
                temparrIndex = (arrIndex + seq) % len(priorities)

        # 해당 우선순위가 없으면 인덱스는 안움직임 그리고 목표 우선순위보다 낮은건 계산안해도됨
        if len(tempArr) != 0 and priorities[location] < n:
            arrIndex = temparrIndex
            answer += len(tempArr)
        # 해당 우선순위일때
        elif n == goalNumber:
            for SelectIndex in tempArr:
                answer += 1
                if SelectIndex == location:
                    return answer

    return answer
