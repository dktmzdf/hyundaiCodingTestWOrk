def solution(arr):
    stk = []
    stk.append(arr[0])
    i = 1
    while i < (len(arr)):
        # print(stk)
        if i < len(arr):
            if len(stk) == 0:
                stk.append(arr[i])
                i += 1
            elif stk[len(stk) - 1] < arr[i]:
                stk.append(arr[i])
                i += 1
            else:
                stk.remove(stk[len(stk) - 1])

    return stk
