def solution(board, skill):
    N = len(board) # 세로
    M = len(board[0]) # 가로
    differ = [[0 for _ in range(M)] for _ in range(N)]

    for type,x1,y1,x2,y2,degree in skill:
        if type == 1:
            degree *= -1

        differ[x1][y1] += degree # 왼쪽 위 모서리, 시작점 표시

        if y2+1 < M:
            differ[x1][y2 + 1] += (degree * -1) # 범위 밖 오른쪽 위 모서리, 끝점 표시

        if x2 +1 < N:
            differ[x2 + 1][y1] += (degree * -1) # 범위 밖 왼쪽 아래 모서리, 끝점 표시

        if x2 + 1 < N and y2 + 1 < M:
            differ[x2 + 1][y2 + 1] += degree # 범위 밖 오른쪽 모서리, 끝점 표시 2차원 때문에 생기는 차이 회복

    # 행에 대해서 부분합 계산하여 differ 갱신
    for x in range(N):
        partSum = 0
        for y in range(M):
            partSum += differ[x][y]
            differ[x][y] = partSum

   # 열에 대해서 부분합 계산하여 differ 갱신
    for y in range(M):
        partSum = 0
        for x in range(N):
            partSum += differ[x][y]
            differ[x][y] = partSum

    answer = 0
    # 모든 칸 연산
    for x in range(N):
        for y in range(M):
            if board[x][y] + differ[x][y] > 0:
                answer += 1

    return answer