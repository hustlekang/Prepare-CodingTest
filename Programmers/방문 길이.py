def solution(dirs):
    cnt = 0
    visit = [[False] * 22 for _ in range(22)]
    differByDirection = {'U': (-2, 0), 'D': (2, 0), 'L': (0, -2), 'R': (0, 2)}
    x, y = 10, 10 # 좌표평면 0,0을 visit[10][10]으로 매핑, 좌표 평면상 1 = visit에서 2로 확대 -> 점과 점 사이 구분 위해서

    for dir in dirs:
        dx, dy = differByDirection[dir]
        nx = x + dx
        ny = y + dy
        if nx < 0 or 22 <= nx or ny < 0 or 22 <= ny:  # 범위 밖 무시
            continue

        mx = (x + nx) // 2
        my = (y + ny) // 2

        if not (visit[x][y] == True and visit[nx][ny] == True and visit[mx][my] == True):
            visit[x][y] = True
            visit[nx][ny] = True
            visit[mx][my] = True
            cnt += 1

        x = nx
        y = ny

    return cnt