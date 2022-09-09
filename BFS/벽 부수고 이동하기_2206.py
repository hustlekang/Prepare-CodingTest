from collections import deque

INF = 10 ** 8
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().strip())))
visit = [[[INF,INF] for _ in range(M) ] for _ in range(N)]
init = (0, 0, 1, False) # x, y, 지나온 칸수, 벽 파괴 여부
visit[0][0][0] = 1
visit[0][0][1] = 1
queue = deque([init])

while queue:
    x, y, cnt, isBroke = queue.popleft()
    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M: # 정상 범위일 때
            if graph[nx][ny] == 0: # 벽이 없을 때
                if isBroke: # 이미 벽을 부셨다면
                    if cnt + 1 < visit[nx][ny][1]: # [1]과 비교
                        visit[nx][ny][1] = cnt + 1
                        queue.append((nx, ny, cnt + 1, isBroke))

                else: # 벽을 부신적이 없으면
                    if cnt + 1 < visit[nx][ny][0]: # [0]과 비교
                        visit[nx][ny][0] = cnt + 1
                        queue.append((nx, ny, cnt + 1, isBroke))

            else: # 벽일 때
                if not isBroke and cnt + 1 < visit[nx][ny][1] : # 부시지 않았을 때만 진행 가능
                    visit[nx][ny][1] = cnt + 1
                    queue.append((nx, ny, cnt + 1, True))

answer = min(visit[-1][-1]) if min(visit[-1][-1]) != INF else -1
print(answer)


################ 시간 초과 코드
from collections import deque

INF = 10 ** 8
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().strip())))
visit = [[INF]*M for _ in range(N)]
init = (0, 0, 1, False) # x, y, 지나온 칸수, 벽 파괴 여부
visit[0][0] = 1
queue = deque([init])

while queue:
    x, y, cnt, isBroke = queue.popleft()
    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        nx, ny = x + dx, y + dy
        # cnt + 1 <= visit[nx][ny] 로 체크하면 시간초과
        # cnt + 1 < visit[nx][ny] 로 체크하면 동일한 칸만큼 지나온 경로인데 벽을 부순 경우와 벽을 안부수고 온 경우체크 불가
        # 그렇기 때문에 <= 로 비교를 해야한다
        # 하지만 시간초과가 나기 때문에 < 로 비교를 해야하므로
        # 벽을 부수고 온 경우와, 벽을 부수지 않고 온 visit을 따로 둬서 체크한다
        # 그럼 지나온 칸이 더 작을 때만 봐도 됨
        if 0 <= nx < N and 0 <= ny < M and  cnt + 1 <= visit[nx][ny]: # 정상 범위 안에 있고 지나온 칸수가 같거나 작을 때
            if graph[nx][ny] == 0: # 벽이 없을 때
                visit[nx][ny] = cnt + 1
                queue.append((nx, ny, cnt + 1, isBroke))

            else: # 벽일 때
                if not isBroke:
                    visit[nx][ny] = cnt + 1
                    queue.append((nx, ny, cnt + 1, True))

answer = visit[-1][-1] if visit[-1][-1] != INF else -1
print(answer)