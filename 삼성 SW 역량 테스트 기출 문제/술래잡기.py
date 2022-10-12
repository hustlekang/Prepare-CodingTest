# 코드트리
# 22년 상반기 오전 1번

def moveRunners():
    global chaser, runners, n
    # 1 : 오른쪽 -1 왼쪽 2 아래쪽 -2 위쪽
    diff = {1 : (0, 1), -1 : (0,-1), 2 : (1,0), -2 : (-1,0)}
    newRunners = []
    for x, y, d in runners:
        if abs(chaser[0] - x) + abs(chaser[1] - y) > 3 :
            newRunners.append((x, y, d))
            continue

        dx, dy = diff[d]
        nx, ny, nd = x + dx , y + dy, d

        if 0 > nx or nx >= n or 0 > ny or ny >= n: # 정삼범위가 아니면
            nd = -d
            nx, ny = x + diff[nd][0], y + diff[nd][1]

        if (nx, ny) != chaser:
            newRunners.append((nx, ny, nd))
        else:
            newRunners.append((x, y, nd))

    runners = newRunners


def moveChaser():
    global cnt, idx, direction, directionIdx, chaser, cntOfChangeDirection, toOutside, keyOfDirection, directionInfo,diff

    dx,dy = 0, 0
    if toOutside:
        dx, dy = diff[0][directionIdx]
    else:
        dx, dy = diff[1][directionIdx]

    chaser = (chaser[0] + dx, chaser[1] + dy)
    cnt += 1
    if cnt == cntOfChangeDirection[idx]:
        if idx == len(cntOfChangeDirection) - 1: # 끝에 도달

            toOutside = not toOutside
            keyOfDirection = int(-1 * keyOfDirection)
            direction = directionInfo[keyOfDirection]
            directionIdx = 0
            cntOfChangeDirection = cntOfChangeDirection[::-1] # 뒤집고
            cnt = 0
            idx = 0
        else:
            cnt = 0
            directionIdx = (directionIdx + 1) % 4 # 방향 변경
            idx += 1


def catch():
    global chaser, runners, diff

    dx, dy = 0, 0
    if toOutside:
        dx, dy = diff[0][directionIdx]
    else:
        dx, dy = diff[1][directionIdx]

    canCatch = set([chaser, (chaser[0] + dx, chaser[1] + dy), (chaser[0] + int(2*dx), chaser[1] + int(2*dy))])
    catchCnt = 0
    newRunners = []

    for x,y,d in runners:
        if (x,y) in canCatch and (x,y) not in trees:
            catchCnt += 1
        else:
            newRunners.append((x,y,d))

    runners = newRunners

    return  catchCnt


if __name__ == '__main__':
    n, m, h, k = map(int, input().split())
    runners = []
    trees = set()

    for _ in range(m):
        x, y, d = map(int, input().split())
        runners.append((x-1, y-1, d))
    for _ in range(h):
        trees.add(tuple(map(lambda x : int(x) - 1, input().split())))

    chaser = (n//2, n//2)

    cntOfChangeDirection = []
    for i in range(1, n):
        cntOfChangeDirection.append(i)
        cntOfChangeDirection.append(i)
    cntOfChangeDirection.append(n-1)

    diff = [
        {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)},  # 가운데서 밖으로
        {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}  # 밖에서 가운대로
    ]
    directionInfo = {1 :['u','r','d','l'] , -1 : ['d','r', 'u', 'l']}
    keyOfDirection = 1
    direction = directionInfo[keyOfDirection]
    directionIdx = 0
    cnt = 0
    idx = 0 # cntOfChangeDirection에서의 인덱스
    toOutside = True

    score = 0

    for trial in range(1, k + 1):
        moveRunners()
        moveChaser()
        score += int(trial * catch())

    print(score)