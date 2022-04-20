# PyPy3
from collections import deque

N = int(input())
graph = []
shark = (-1, -1)
sharkSize = 2
eatCnt = 0
sec = 0
queue = deque([])
isFound = False

for i in range(N):
    line = list(map(int, input().split()))
    graph.append(line)
    if not isFound:  # 상어 위치 찾을 때까지만
        for j in range(N):
            if line[j] == 9:
                shark = (i, j)
                isFound = True

while True:
    eatableFishes = []
    for x in range(N):
        for y in range(N):
            if 1 <= graph[x][y] < sharkSize:  # 물고기까지 거리와 물고기의 좌표를 알아야함
                distance = 0
                visit = [[False] * N for _ in range(N)]
                visit[x][y] = True
                queue.append((x, y, 0))

                while queue:  # 물고기에서 상어까지의 거리를 계산
                    r, c, d = queue.popleft()
                    if (r, c) == shark:
                        distance = d
                        queue.clear()
                        break

                    for dr, dc in zip([0, 0, -1, 1], [1, -1, 0, 0]):
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < N and 0 <= nc < N and (graph[nr][nc] <= sharkSize or graph[nr][nc] == 9) and not visit[nr][nc]:
                            visit[nr][nc] = True
                            queue.append((nr, nc, d + 1))
                if distance > 0:
                    eatableFishes.append((x, y, distance))

    if len(eatableFishes) == 0:  # 더 이상 먹을 물고기 없으면 종료
        break

    else:  # 먹을수 있는게 있으면
        if len(eatableFishes)>1:
            eatableFishes.sort(key=lambda x: x[1])  # 가장 왼쪽
            eatableFishes.sort(key=lambda x: x[0])  # 가장 위에
            eatableFishes.sort(key=lambda x: x[2])  # 가장 가까운

        fish = eatableFishes[0]
        sec += fish[2]  # 먹으러 가는 시간 더하고
        eatCnt += 1  # 먹은 물고기 추가
        graph[shark[0]][shark[1]] = 0  # 상어 있던 위치 0으로 만들고
        shark = (fish[0], fish[1])  # 상어 위치 이동
        graph[shark[0]][shark[1]] = 9  # 새로운 상어 위치 갱신

        if eatCnt == sharkSize:  # 상어 크기만큼 먹으면 상어 크기 증가
            sharkSize += 1
            eatCnt = 0

print(sec)