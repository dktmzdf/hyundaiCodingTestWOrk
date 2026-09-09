def solution(num_list, n):
    answer = []
    tempArr = []
    for idx in range(len(num_list)):
        if n <= idx:
            answer.append(num_list[idx])
        else:
            tempArr.append(num_list[idx])
    print(answer.extend(tempArr))
    return answer
