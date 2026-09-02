def solution(l, r):
    answer = []
    for num in range(l, r + 1):
        if num % 5 == 0:
            answer.append(num)
            for digit in str(num):
                if digit != "5" and digit != "0":
                    answer.remove(num)
                    break

    if not answer:
        return [-1]

    return answer


# 일단 범위 l과 r 사이의 모든 숫자를 확인하면서, 각 숫자가 5로만 이루어져 있는지 확인해야 합니다.
# 따라서 우리는 가장 큰수가 뭔지 확인부터 해야한다.
# 일단
