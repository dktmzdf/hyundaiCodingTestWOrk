def solution(my_string, is_prefix):
    decomposition = []
    arr = list(my_string)
    for idx in range(1, len(arr)):
        decomposition.append(my_string[0:idx])

    return decomposition.count(is_prefix)
