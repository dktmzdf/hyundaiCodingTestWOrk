import heapq


def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    h = lambda p: abs(p[0] - goal[0]) + abs(p[1] - goal[1])  # Manhattan

    open_heap = [(h(start), 0, start)]  # (f, g, node)
    came_from = {}
    g_score = {start: 0}

    while open_heap:
        f, g, cur = heapq.heappop(open_heap)
        if cur == goal:
            path = [cur]
            while cur in came_from:
                cur = came_from[cur]
                path.append(cur)
            return len(path)
        if g > g_score.get(cur, float("inf")):  # stale entry 스킵
            continue
        r, c = cur
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                ng = g + 1
                if ng < g_score.get((nr, nc), float("inf")):
                    g_score[(nr, nc)] = ng
                    came_from[(nr, nc)] = cur
                    heapq.heappush(open_heap, (ng + h((nr, nc)), ng, (nr, nc)))
    return -1  # 경로 없음


def solution(maps):
    answer = 0
    return astar(maps, (0, 0), (len(maps) - 1, len(maps[0]) - 1))
