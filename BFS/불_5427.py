from collections import deque
import sys

# 큐에 든 모든 불들을 이동시키고 새롭게 이동한 불을 다시 큐에 삽입
def fireMove():
    global graph, fires, w, h
    n = len(fires) # 현재 초의 모든 불들의 개수
    for _ in range(n):
        x, y = fires.popleft()
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == '.' : # 빌딩 안에 있고 빈 공간 일때만 이동
                graph[nx][ny] = '*'
                fires.append((nx, ny)) # 새롭게 이동한 불은 다시 큐에 삽입

# 큐에 든 모든 위치를 이동시키고 다시 큐에 삽입
# 빌딩을 벗어나면 이동횟수 반환
def personMove():
    global graph, queue, visit
    n = len(queue) # 현재 초의 모든 위치
    for _ in range(n):
        x, y, cnt = queue.popleft()
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w: # 정삼 범위 일 때
                if graph[nx][ny] == '.' and not visit[nx][ny]: # 빈 공간 일때만
                    queue.append((nx, ny, cnt + 1))
                    visit[nx][ny] = True
            else: # 빌딩을 벗어나면
                return cnt + 1

    return 'IMPOSSIBLE'

if __name__ == '__main__':
    trial = int(sys.stdin.readline())

    for _ in range(trial):
        fires = deque([]) # 불들의 좌표
        person = (-1, -1)
        w, h = map(int, sys.stdin.readline().split())

        graph = []
        for i in range(h):
            row = sys.stdin.readline().strip()
            for j in range(w):
                if row[j] == '*':  # 초기 불 위치 기록
                    fires.append((i, j))
                elif row[j] == '@':  # 초기 사람 위치 기록
                    person = (i, j)

            graph.append(list(row))

        graph[person[0]][person[1]] = '.'  # 상근이 위치도 빈 공간으로 설정
        init = (person[0], person[1], 0)  # (x, y, cnt)  상근이의 위치
        queue = deque([init])
        visit = [[False] * w for _ in range(h)] # 상근이 방문 여부
        answer= 'IMPOSSIBLE'

        while queue:
            fireMove()
            answer = personMove()
            if answer != 'IMPOSSIBLE':
                break

        print(answer)