def solution(n):
    answer = 0
    if n % 2 == 0:  # n is even
        for i in range(2, n + 1, 2):
            answer += i ** 2
    else:  # n is odd
        for i in range(1, n + 1, 2):
            answer += i
    return answer
