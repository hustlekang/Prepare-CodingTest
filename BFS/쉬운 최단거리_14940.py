import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split(' '))

    answer = [[-1] * m for _ in range(n)]
    visit = [[False] * m for _ in range(n)]
    graph = []
    queue = deque([])

    for i in range(n):
        line = input().strip().split(' ')
        graph.append(line)

        for j in range(m):
            if graph[i][j] == '0':
                answer[i][j] = 0

            if queue: continue
            if line[j] == '2':
                queue.append((i, j, 0))
                visit[i][j] = True
                answer[i][j] = 0

    while queue:
        x, y , d = queue.popleft()

        for dx, dy in zip([0,0,-1,1], [1,-1,0, 0]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and graph[nx][ny] == '1':
                visit[nx][ny] = True
                answer[nx][ny] = d + 1
                queue.append((nx, ny, d + 1))

    for line in answer:
        print(" ".join(map(str,line)))