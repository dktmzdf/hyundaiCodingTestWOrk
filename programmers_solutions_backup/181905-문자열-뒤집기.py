def solution(my_string, s, e):
    answer = ""
    arr = list(my_string)
    reverseArr = []
    for idx in range(e, s - 1, -1):
        reverseArr.append(my_string[idx])

    for idx in range(len(reverseArr)):
        arr[s + idx] = reverseArr[idx]

    return "".join(arr)
