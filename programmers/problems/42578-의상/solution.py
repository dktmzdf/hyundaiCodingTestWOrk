def solution(clothes):
    # 계산은dic 검사하면 될듯
    # 키값을 서로 문자열 더하면 될듯 - 아니 그냥 조합갯수 구하면 될듯?
    # sortedClothes = sorted(clothes, key=lambda x: x[1])
    dic = {}
    for clothe in clothes:
        if clothe[1] in dic:
            dic[clothe[1]] += 1
        else:
            dic[clothe[1]] = 1

    answer = 1
    for count in dic.values():
        answer *= count + 1  # 안입는 경우 추가

    return answer - 1  # 다 안 입는다는 없음
