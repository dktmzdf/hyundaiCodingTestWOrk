# 해시 문제
def solution(nums):
    answer = 0
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # print(len(dic))
    # print(dic.keys())
    if len(nums) / 2 < len(dic):
        return len(nums) / 2
    else:
        return len(dic)
