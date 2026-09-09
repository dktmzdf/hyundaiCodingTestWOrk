def solution(str_list, ex):
    answer = ""
    for block in str_list:
        # print(block[len(block) - len(ex) : len(block)])
        if block.find(ex) == -1:
            answer += block

    return answer
