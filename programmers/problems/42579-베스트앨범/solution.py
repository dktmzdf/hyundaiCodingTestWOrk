def solution(genres, plays):
    answer = []
    songDic = {}
    # 집어 넣을때 고유번호 작은 순서대로 집어 넣고 또 파이썬 정렬은 안정되어 있어 따로 고유번호는 정렬 할 필요가 없음
    for idx in range(len(genres)):
        if genres[idx] in songDic:
            songDic[genres[idx]].append((idx, plays[idx]))
        else:
            tempArr = [(idx, plays[idx])]
            songDic[genres[idx]] = tempArr

    keySort = sorted(
        songDic, key=lambda x: sum(play for idx, play in songDic[x]), reverse=True
    )

    # print(keySort)
    for key, value in songDic.items():
        # 재생 횟수 정렬
        songDic[key] = sorted(value, key=lambda x: x[1], reverse=True)

    # print(songDic)
    for key in keySort:
        for n in range(0, min(2, len(songDic[key]))):
            answer.append(songDic[key][n][0])

    return answer
