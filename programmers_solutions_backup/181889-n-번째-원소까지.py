def solution(num_list, n):
    answer = []
    for idx in range(len(num_list)):
        if n > idx:
            answer.append(num_list[idx])
    #print(answer)
    return answer
