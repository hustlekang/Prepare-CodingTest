import sys
from collections import deque

input = sys.stdin.readline

# 인수 graph에서 [x][y]의 상하좌우가 0인 갯수를 반환
def getAdjacent(x, y, graph):
    cnt = 0

    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                cnt += 1

    return cnt

# 빙산들의 덩어리를 계산하는 함수
def countPart(points):
    cnt = 0
    visit = [[False] * M for _ in range(N)]
    queue = deque([])

    for point in points:
        if not visit[point[0]][point[1]]:
            queue.append(point)
            visit[point[0]][point[1]] = True
            cnt += 1

            while queue:
                x, y = queue.popleft()
                for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and graph[nx][ny] != 0:
                        visit[nx][ny] = True
                        queue.append((nx, ny))
    return cnt

# 모든 빙산을 녹이는 함수, 녹은 뒤 남아있는 빙산을 반환
def melt(points):
    allMelted = set()
    copy = [graph[i][:] for i in range(N)]
    for x, y in points:
        graph[x][y] -= getAdjacent(x, y, copy)
        if graph[x][y] <= 0:
            graph[x][y] = 0
            allMelted.add((x, y))

    newPoints = points - allMelted

    return newPoints

if __name__ == '__main__':
    N, M = map(int, input().split(' '))
    graph = []
    points = set()
    for i in range(N):
        row = list(map(int, input().split(' ')))
        graph.append(row)
        for j in range(M):
            if row[j] != 0:
                points.add((i, j))

    cnt = 0
    parts = 1

    while parts < 2:
        points = melt(points)
        cnt += 1
        parts = countPart(points)

        if not points:
            cnt = 0
            break

    print(cnt)