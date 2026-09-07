def solution(num_list):
    odd = 0
    even = 0
    for idx in range(len(num_list)):
        if (idx + 1) % 2 == 1:
            odd += num_list[idx]
        elif (idx + 1) % 2 == 0:
            even += num_list[idx]

    if even <= odd:
        return odd
    elif odd < even:
        return even
