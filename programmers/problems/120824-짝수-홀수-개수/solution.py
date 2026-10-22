def solution(num_list):
    answer = []
    odd_n = 0
    even_n = 0
    for i in num_list:
        if i % 2 == 0:
            even_n += 1
        else:
            odd_n += 1
    answer.append(even_n)
    answer.append(odd_n)
    return answer
