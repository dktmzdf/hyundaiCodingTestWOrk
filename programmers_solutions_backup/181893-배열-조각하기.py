# def solution(arr, query):
#     answer = arr
#     tempArr = []

#     for pivotIndex in range(len(query)):
#         # print()
#         # print(answer)
#         # 짝수
#         if pivotIndex % 2 == 0:
#             for num in answer:
#                 tempArr.append(num)
#                 if num == query[pivotIndex]:
#                     break

#         # 홀수
#         else:
#             for num in reversed(answer):
#                 tempArr.append(num)
#                 if num == query[pivotIndex]:
#                     tempArr.reverse()
#                     break
#         # print(f"tempArr{tempArr}")
#         # 넣기
#         answer.clear()
#         for num in tempArr:
#             answer.append(num)

#         # print(answer)
#         tempArr.clear()
#         # print(answer)


#     return answer
def solution(arr, query):
    for i, q in enumerate(query):
        if i % 2 == 0:
            arr = arr[: q + 1]
        else:
            arr = arr[q:]
    return arr
