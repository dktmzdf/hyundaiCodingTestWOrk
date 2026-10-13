# 위아래로 계산해보기
# 좌우로는 한칸씩이지 뭐...

# 에러
# def solution(name):

#     answer = 0
#     temp_name = ["A"] * len(name)
#     # print(temp_name)
#     # print("".join(temp_name))
#     name_index = 0

#     while True:
#         forward_step = ord(name[name_index]) - ord("A")
#         backward_step = ord("Z") - ord(name[name_index]) + 1
#         # 양방향
#         # print(forward_step)
#         # print(backward_step)
#         answer += forward_step if forward_step <= backward_step else backward_step
#         temp_name[name_index] = name[name_index]

#         # 전부 같으면 좌우계산 필요없음
#         if "".join(temp_name) == name:
#             break

#         # 좌우계산
#         select_index = 0
#         add_answer = 0
#         # 정방향
#         for next_index in range(0, len(name)):
#             # print(next_index)
#             # 다른놈 찾기
#             if temp_name[next_index] != name[next_index]:
#                 forward_index = next_index - name_index  # 순방향으로 갈때
#                 backward_index = len(name) - next_index + name_index  # 역방향으로 갈떄
#                 # print(backward_index)
#                 add_answer = (
#                     forward_index if forward_index <= backward_index else backward_index
#                 )
#                 select_index = next_index
#                 break
#         # 역방향
#         for previous_index in range(len(name) - 1, -1, -1):
#             # print(next_index)
#             # 다른놈 찾기
#             if temp_name[previous_index] != name[previous_index]:

#                 test +


#                 forward_index = name_index - previous_index  # 순방향으로 갈때
#                 backward_index = (
#                     len(name) - previous_index + name_index
#                 )  # 역방향으로 갈떄
#                 previous_add_index = (
#                     forward_index if forward_index <= backward_index else backward_index
#                 )
#                 # print(backward_index)
#                 if add_answer < previous_add_index:
#                     add_answer = previous_add_index
#                     select_index = previous_index
#                 break

#         answer += add_answer
#         name_index = select_index


#     return answer


# 대체 이걸 어떻게 하는겨?
# 나중에 다시봐야지
def solution(name):
    n = len(name)
    updown = sum(min(ord(c) - 65, 91 - ord(c)) for c in name)

    move = n - 1  # 오른쪽으로만 쭉
    for i in range(n):
        nxt = i + 1
        while nxt < n and name[nxt] == "A":
            nxt += 1
        move = min(move, 2 * i + (n - nxt), i + 2 * (n - nxt))

    return updown + move
