def solution(str_list):
    answer = []
    for idx in range(len(str_list)):
        if str_list[idx] == "l":
            answer.extend(str_list[0:idx])
            break
        elif str_list[idx] == "r":
            answer.extend(str_list[idx + 1 : len(str_list)])
            break
    #print(answer)
    return answer
