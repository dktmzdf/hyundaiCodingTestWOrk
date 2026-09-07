def solution(rank, attendance):
    rankDic = {}
    for idx in range(len(attendance)):
        if attendance[idx] == True:
            rankDic[idx] = rank[idx]

    rankDic = sorted(rankDic.items(), key=lambda item: item[1], reverse=False)

    return 10000 * rankDic.pop(0)[0] + 100 * rankDic.pop(0)[0] + rankDic.pop(0)[0]
