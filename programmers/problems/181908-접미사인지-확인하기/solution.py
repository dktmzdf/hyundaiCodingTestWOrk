def solution(my_string, is_suffix):
    answer = 0
    decomposition = []
    arr = list(my_string)
    for idx in range(len(arr)):
        decomposition.append(my_string[idx : len(my_string)])

    return decomposition.count(is_suffix)
