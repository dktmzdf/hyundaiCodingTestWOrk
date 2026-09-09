def solution(num_list):
    answer = 0
    evenStr = ""
    oddStr = ""
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            evenStr += str(num_list[i])
        else:
            oddStr += str(num_list[i])

    answer = int(evenStr) + int(oddStr)
    return answer
