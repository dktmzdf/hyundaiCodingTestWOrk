def solution(my_string, m, c):
    div2 = []
    repeatCount = len(my_string) // m

    if (len(my_string) % m) != 0:
        repeatCount += 1

    for col in range(repeatCount):
        arr = []
        for row in range(m):
            arr.append(my_string[col * m + row])
        div2.append(arr)

    answer = []
    for idx in range(len(div2)):
        answer.append(div2[idx][c - 1])

    return "".join(answer)
