def solution(num_list):
    answer = num_list;
    # for i in range(len(num_list)):
    #     if num_list[i] > num_list[-1] :
    #         answer.append(num_list[i] - num_list[-1])
    #     else:
    #         answer.append(num_list[i]*2)
    if num_list[-1] > (num_list[-2]):
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1]*2)
    
    
    return answer
