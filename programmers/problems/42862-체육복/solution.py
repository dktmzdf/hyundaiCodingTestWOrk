def solution(n, lost, reserve):
    answer = 0
    studentArray = [1 for _ in range(n)]

    #print(studentArray)

    for removeIdx in lost:
        studentArray[removeIdx - 1] = 0

    #print(studentArray)

    for addIdx in reserve:
        studentArray[addIdx - 1] += 1

    #print(studentArray)

    # 여기까진 일단 초기값 설정

    for idx in range(n):
        if studentArray[idx] == 0:
            if idx != 0 and studentArray[idx - 1] > 1:
                studentArray[idx - 1] -= 1
                studentArray[idx] == 1
                answer += 1
            elif idx != n - 1 and studentArray[idx + 1] > 1:
                studentArray[idx + 1] -= 1
                studentArray[idx] == 1
                answer += 1
        else:
            answer += 1

    return answer
