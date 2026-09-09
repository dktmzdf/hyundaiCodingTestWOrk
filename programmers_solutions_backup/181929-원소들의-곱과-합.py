def solution(num_list):
    answer = 0
    sum = 0
    multiply = 1
    for i in range(len(num_list)):
        sum += num_list[i]
        multiply *= num_list[i]

    if multiply < sum**2:
        answer = 1
    else:
        answer = 0
    return answer
