# 여기선 그냥 배열 순회하는거에 가까우니 ...
# + - 완전 탐색
# 재귀 함수 정의... current_sum를 받게
# 재귀 끝은 인덱스가 배열 길이와 같아지면 돌려줌
# 함수 두번 호출 하나는 +로 더하게 다른 하나는 -로 뺴기
# 두갈래로 쭉 나가면 뭔가 만나긴 하겠지 맞으면 visited list에 적어넣고 갯수세면 일단 될듯?
def dfs_recursive(graph, start, current_sum, target, visited=None):
    if visited is None:
        visited = []

    if start < len(graph):
        dfs_recursive(graph, start + 1, current_sum + graph[start], target, visited)
        dfs_recursive(graph, start + 1, current_sum - graph[start], target, visited)
    else:
        if current_sum == target:
            visited.append(1)

    return visited


def solution(numbers, target):
    return len(dfs_recursive(numbers, 0, 0, target))
