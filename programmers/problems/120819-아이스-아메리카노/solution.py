def solution(money):
    answer = []
    count = money // 5500
    round = money - (5500 * count)
    return [count, round]
