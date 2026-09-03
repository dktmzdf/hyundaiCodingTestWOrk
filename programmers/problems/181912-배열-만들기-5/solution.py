def solution(intStrs, k, s, l):
    answer = []

    for intSeq in intStrs:
        if k < int(intSeq[s : s + l]):
            answer.append(int(intSeq[s : s + l]))
    return answer
