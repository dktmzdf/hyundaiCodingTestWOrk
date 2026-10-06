from functools import cmp_to_key

def solution(numbers):
    strs = list(map(str, numbers))
    strs.sort(key=cmp_to_key(lambda a, b: (a + b < b + a) - (a + b > b + a)))
    return "0" if strs[0] == "0" else "".join(strs)

# def solution(numbers):
#     # 음....  일단 자리수가 적은 애들부터 가장 큰값을 미루어야 됨 9, 9, 9, 1000 이라고 하면 9991000이 가장 크거든
#     # 먼저 따로 배열을 복사후 계산하면서 이미 계산된건 -1로 바꾸면 될듯
#     # 잘못 생각함 아무래도 가장 큰 자리수를 가장 큰놈이 정렬해야할듯

#     # 설마 파이썬에서 전부 문자열로 바꾸고 정렬하면 알아서 되던가?
#     # 아 진짜네;; 이거 문자열로 바꾸고 정렬하면 양쪽 더해서 비교해서 정렬하면 잘됨 ㅎㅎ
#     answer = ""
#     for i in range(1, len(numbers)):
#         for j in range(i, 0, -1):
#             temp_1 = str(numbers[j]) + str(numbers[j - 1])
#             temp_2 = str(numbers[j - 1]) + str(numbers[j])
#             if temp_1 > temp_2:
#                 numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
#             else:
#                 break
#     # print(numbers)

#     for n in numbers:
#         answer += str(n)

#     return "0" if answer[0] == "0" else answer


