def solution(arr):
    answer = arr

    # len(arr) col
    # len(arr[0]) row
    if len(arr) == len(arr[0]):
        return arr
    elif len(arr) > len(arr[0]):
        for rowIndex in range(len(arr)):
            for n in range(len(arr) - len(arr[rowIndex])):
                answer[rowIndex].append(0)
    elif len(arr) < len(arr[0]):
        for s in range(len(arr[0]) - len(arr)):
            tempArr = []
            for n in range(len(arr[0])):
                tempArr.append(0)
            answer.append(tempArr)

    return answer


def solution_AI(arr):
    rows, cols = len(arr), len(arr[0])
    size = max(rows, cols)

    answer = [row + [0] * (size - cols) for row in arr]
    answer += [[0] * size for _ in range(size - rows)]

    return answer
