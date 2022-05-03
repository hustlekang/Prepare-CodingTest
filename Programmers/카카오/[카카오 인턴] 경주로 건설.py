from collections import deque

def solution(board):
    def search(start):
        N = len(board)
        answer = 10 ** 6
        way = {  # dx,dy에 따른 진행 방향
            (0, 1): 'r',
            (1, 0): 'd',
            (0, -1): 'l',
            (-1, 0): 'u'
        }

        # 방문처리 할때 현재 [x][y]까지의 비용을 저장한다
        visit = [[answer] * N for _ in range(N)]
        visit[0][0] = 0

        queue = deque([start])  # (x,y,방향,비용)

        while queue:
            node = queue.popleft()
            x, y, direction, money = node

            for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]):
                nx = x + dx
                ny = y + dy
                newDirection = way[(dx, dy)]
                cost = money + 100
                if direction != newDirection:  # 방향이 바뀌면 코너이기 때문에 500원 증가
                    cost += 500

                # 현재 방문 비용 이하면 재탐색 허용, 최초 방문도 큰 값으로 초기화 해놔서 작음
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and cost < visit[nx][ny]:
                    visit[nx][ny] = cost
                    queue.append((nx, ny, newDirection, cost))

        answer = visit[N-1][N-1]
        return answer

    return min([search((0, 0, 'r', 0)), search((0, 0, 'd', 0))]) # 0,0 에서 아래로 시작, 오른쪽으로 시작 2가지 중 작은 답