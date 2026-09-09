def solution(n):
    answer = [[0] * n for _ in range(n)]

    # n*n 2차원 배열 정사각형 그리고 채워지는건 1 ~ n**2-1 까지임
    # 설명을 보면 시계방향으로 돌아감
    # 일단 처음엔 n만큼 가고 그다음 아래로 n - 1 다음도 n - 1까지 가나 그다음부터 n-2만큼감
    # 4, 3,3,2,2,1,1
    # 처음 [0][0] ~ [0][n] 그다음 [1][n] ~ [n][n] 그다음
    # [n][n-1] ~ [n][0] 그다음 [n-1][0] ~ [1][0] 그다음 [1][1]...
    # 방향 d = 0 오른쪽 d = 1 아래쪽 d = 2 왼쪽 d = 3 위쪽

    num = 0
    d = 0
    distance = n

    while True:

        df4 = d // 4
        # 오른쪽
        if d % 4 == 0:
            for i in range(df4, n - df4):
                num += 1
                answer[df4][i] = num
        # 아래
        elif d % 4 == 1:
            for i in range(df4 + 1, n - df4):
                num += 1
                answer[i][(n - 1) - (df4)] = num
        # 왼쪽
        elif d % 4 == 2:
            for i in range(df4 + 1, n - df4):
                num += 1
                answer[(n - 1) - (df4)][(n - 1) - i] = num
        # 윗쪽
        elif d % 4 == 3:
            for i in range(df4 + 1, n - (df4) - 1):
                num += 1
                answer[(n - 1) - i][df4] = num

        d += 1  # 방향 바꾸기
        if (d + 1) % 2 == 0:  # 규칙를 보니 방향 두번바꾸면 거리가 -1만큼 줄어듬
            distance -= 1

        if distance == 0:
            break

    # for sss in answer:
    #     print(sss)

    return answer


def solution_AI(n):
    answer = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            answer[top][col] = num
            num += 1
        top += 1

        for row in range(top, bottom + 1):
            answer[row][right] = num
            num += 1
        right -= 1

        for col in range(right, left - 1, -1):
            answer[bottom][col] = num
            num += 1
        bottom -= 1

        for row in range(bottom, top - 1, -1):
            answer[row][left] = num
            num += 1
        left += 1

    return answer
