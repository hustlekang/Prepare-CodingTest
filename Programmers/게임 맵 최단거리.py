from collections import deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    visit = [[False] *m for _ in range(n)]
    directionX = [1, -1, 0, 0]
    directionY = [0, 0, 1, -1]
    queue = deque([(0, 0, 1)])
    visit[0][0] = True

    while (queue):
        x, y, distance = queue.popleft()

        if x == n - 1 and y == m - 1:
            answer = distance
            break

        for dx, dy in zip(directionX, directionY):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == False and maps[nx][ny] == 1:
                visit[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return answer