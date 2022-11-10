import sys
from collections import deque
input = sys.stdin.readline

def moveWalls():
    global walls
    newWalls = set()

    for x, y in walls:
        nx = x + 1
        if nx == 8:
            continue
        newWalls.add((nx, y))

    walls = newWalls


if __name__ == '__main__':
    answer = 0
    walls = set()
    visit = [[False] * 8 for _ in range(8)]
    queue = deque([(7, 0)])

    for i in range(8):
        row = input().strip()
        for j in range(8):
            if row[j] == '#':
                walls.add((i, j))

    cnt = 0
    moveWallCnt = 1
    newMoveWallCnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1

        if (x,y) == (0,7):
            answer = 1
            break

        if (x,y) not in walls: # 사람 위치에 벽이 있으면 이동 불가
            # 사람 이동
            for dx, dy in zip([0,0,1,-1,1,1,-1,-1],[1,-1,0,0,1,-1,1,-1]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 8 and 0 <= ny < 8 and not visit[nx][ny] and (nx, ny) not in walls:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    newMoveWallCnt += 1

            queue.append((x, y)) # 제자리
            newMoveWallCnt += 1

        if cnt == moveWallCnt: # 1초 단위 사람 모두 이동 마치면
            moveWalls() # 벽 이동
            moveWallCnt = newMoveWallCnt
            cnt = 0
            newMoveWallCnt = 0
            visit = [[False] * 8 for _ in range(8)] # 턴 바뀔때마다 visit 초기화

    print(answer)