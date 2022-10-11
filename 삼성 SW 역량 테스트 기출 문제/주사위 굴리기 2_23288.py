from collections import deque

def move():
    global position, direction
    x,y = position

    if direction == 'e':
        if y + 1 == M:
            direction = 'w'
            move()

        else:
            # 이동 후 리턴
            position = (x, y + 1)
            a, b, c, d = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
            dice[1][1] = a
            dice[1][2] = b
            dice[3][1] = c
            dice[1][0] = d
            return

    elif direction == 'w':
        if y -1 == -1:
            direction = 'e'
            move()

        else:
            position = (x, y - 1)
            a, b, c, d = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
            dice[3][1] = a
            dice[1][0] = b
            dice[1][1] = c
            dice[1][2] = d
            return

    elif direction == 'n':
        if x -1 == -1:
            direction = 's'
            move()

        else:
            position = (x -1, y)
            a, b, c, d = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
            dice[3][1] = a
            dice[0][1] = b
            dice[1][1] = c
            dice[2][1] = d
            return

    else:
        if x + 1 == N:
            direction = 'n'
            move()

        else:
            position = (x + 1, y)
            a, b, c, d = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
            dice[1][1] = a
            dice[2][1] = b
            dice[3][1] = c
            dice[0][1] = d
            return


def getScore():
    global position
    x, y = position
    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True
    cnt = 1
    queue = deque([position])
    number = graph[x][y]

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip([0,0,-1,1],[1,-1,0,0]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and graph[nx][ny] == number:
                visit[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    score = int(number * cnt)
    return score


def changeDirection():
    global direction
    directionArr = ['e','s','w','n']
    x, y = position
    bottomNum = dice[3][1] # A
    blockNum = graph[x][y] # B

    if bottomNum > blockNum: #90도 시계 회전
        idx = (directionArr.index(direction) + 1) % 4
        direction = directionArr[idx]

    elif bottomNum < blockNum: #90도 반시계 회전
        idx = (directionArr.index(direction) + 3) % 4
        direction = directionArr[idx]


if __name__ == '__main__':
    N, M, K = map(int, input().split(' '))
    graph = [list(map(int,input().split(' '))) for _ in range(N)]
    score = 0
    position = (0, 0)
    direction = 'e'
    dice = [
        [0,2,0],
        [4,1,3],
        [0,5,0],
        [0,6,0]
    ]

    for _ in range(K):
        move()
        score += getScore()
        changeDirection()

    print(score)