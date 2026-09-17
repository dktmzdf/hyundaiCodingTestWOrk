def solution(array, commands):
    answer = []
    # 커맨드 하나하나 뽑아서 슬라이스 한 후 정렬떄리면 될듯
    # 커맨드 하나하나는 for문

    for command in commands:
        sliceArr = array[command[0] - 1 : command[1]]
        temp = sorted(sliceArr)
        print(temp)
        answer.append(temp[command[2] - 1])

    return answer
