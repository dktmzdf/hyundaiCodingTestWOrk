def solution(num_list):
    answer = 0
    count = 0
    for num in num_list:
        numValue = num
        while numValue != 1:
            count += 1
            if numValue % 2 == 0:
                numValue = int(numValue / 2)
            elif numValue % 2 == 1:
                numValue = int((numValue - 1) / 2)
    return count
