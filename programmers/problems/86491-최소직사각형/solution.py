def solution(sizes):
    answer = 0
    # 이걸 가로로 잡자 가장 긴거 하나는 잡아줘야됨
    # 최솟값에서 가장 큰수 이걸 세로로 잡자...어떻게 할까?
    width = 0  # 가장 큰수
    height = 0  # 최솟값에서 가장 큰수
    for size in sizes:
        largeN = size[0] if size[0] >= size[1] else size[1]
        smallN = size[0] if size[0] < size[1] else size[1]
        if width < largeN:
            width = largeN

        if height < smallN:
            height = smallN
    return width * height
