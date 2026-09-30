def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in range(len(graph[start])):
        if nxt not in visited and graph[start][nxt] == 1:
            dfs_recursive(graph, nxt, visited)
    return visited


def solution(n, computers):
    answer = 0
    # 입력이 이차원 배열임 각 노드마다 연결되어있는 걸 표현함 1은 연결 0은 연결 안됨
    # 먼저 BFS로 시작노드부터 쭉 흛어보는게 좋으듯
    # 근데 찾아낸 네트워크를 결과값을 어따 저장하지?음..... 먼저 DICT으로 찾아낸 노드를 할수있다 치고........
    # 근데 어쩌피 찾아내기만 하면 상관없지 않나?.... 내 생각앤 그냥 네트워크 어떤지 알바아닌듯

    # 찾아낸건 할 필요가 없으니 일단 캐시는 해놔야겠다
    cacheVisited = set()
    for idx in range(n):
        if idx not in cacheVisited:
            # print(idx)
            answer += (
                1  # 여기 들어왔다는건 연결되지 않았단 소리니 따로 네트워크가 있다는것
            )
            cacheVisited = dfs_recursive(computers, idx, cacheVisited)
            # print(cacheVisited)

    return answer
