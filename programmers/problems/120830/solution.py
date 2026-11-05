def solution(n, k):
    answer = 0
    meet = n * 12000
    service_drink = n // 10
    drink = 2000 * (k - service_drink)
    if drink < 0:
        drink = 0
    answer = meet + drink
    
    return answer