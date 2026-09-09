def solution(n, slicer, num_list):
    answer = []

    if n == 1:
        # n = 1 : num_list의 0번 인덱스부터 b번 인덱스까지
        answer = list(num_list[0 : slicer[1] + 1])
    elif n == 2:
        # n = 2 : num_list의 a번 인덱스부터 마지막 인덱스까지
        answer = list(num_list[slicer[0] :])
    elif n == 3:
        # n = 3 : num_list의 a번 인덱스부터 b번 인덱스까지
        answer = list(num_list[slicer[0] : slicer[1] + 1])
    elif n == 4:
        # n = 4 : num_list의 a번 인덱스부터 b번 인덱스까지 c 간격으로
        answer = list(num_list[slicer[0] : slicer[1] + 1 : slicer[2]])

    return answer
