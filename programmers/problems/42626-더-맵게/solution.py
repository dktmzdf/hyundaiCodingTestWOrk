import heapq


# 은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
def solution(scoville, K):
    q = []

    for n in scoville:
        heapq.heappush(q, n)

    count = 0
    if len(q) > 1:
        # print(q)

        # 한개면 조합 못함
        while len(q) > 1:
            checkHeapNum = heapq.heappop(q)
            # 최소힙에서 Pop한 값이 5이하면 최소값이 5를 못넘는다는 소리
            if checkHeapNum < K:
                heapq.heappush(q, checkHeapNum)
            else:
                return count

            count += 1
            minSco_1 = heapq.heappop(q)
            minSco_2 = heapq.heappop(q)
            mixtureSco = minSco_1 + (minSco_2 * 2)
            heapq.heappush(q, mixtureSco)

    if len(q) == 1 and q[0] >= K:
        return count
    else:
        return -1
