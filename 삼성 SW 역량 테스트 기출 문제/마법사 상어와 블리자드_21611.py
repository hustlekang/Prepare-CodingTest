from collections import  deque
def iceAttack(d, s):
    diff = {
        1 : (-1,0),
        2 : (1,0),
        3 : (0,-1),
        4 : (0,1)
    }
    x, y = shark
    dx, dy = diff[d]
    for _ in range(s):
        x, y = x + dx, y + dy
        graph[x][y] = 0 # 구슬 파괴


def move():
    # queue에다가 가운데 부터 0이 아닌 구슬들 순서대로 넣어줌
    queue = deque([0]) # 상어 넣고
    diff = [(0,-1), (1,0), (0,1), (-1,0)]
    x, y = shark
    diffIdx = 0

    cnt = 0
    changeCnt = 1
    trial = 0 # 2회 가야함

    while True:
        dx, dy = diff[diffIdx]
        x , y = x + dx, y + dy

        if x < 0 or N <= x or y < 0 or N <= y:
            break

        if graph[x][y] != 0:
            queue.append(graph[x][y])

        cnt += 1

        if cnt == changeCnt:
            diffIdx = (diffIdx + 1) % 4
            cnt = 0
            trial += 1

        if trial == 2:
            trial = 0
            cnt = 0
            changeCnt += 1

    # 그대로 다시 넣어준다
    x, y = shark
    diffIdx = 0

    cnt = 0
    changeCnt = 1
    trial = 0  # 2회 가야함
    queueIdx = 1
    length = len(queue)

    while True:
        dx, dy = diff[diffIdx]
        x , y = x + dx, y + dy

        if x < 0 or N <= x or y < 0 or N <= y:
            break

        # 가운데로 당겨서 빈 곳은 0으로
        if queueIdx >= length:
            graph[x][y] = 0
        else:
            graph[x][y] = queue[queueIdx]

        queueIdx += 1
        cnt += 1

        if cnt == changeCnt:
            diffIdx = (diffIdx + 1) % 4
            cnt = 0
            trial += 1

        if trial == 2:
            trial = 0
            cnt = 0
            changeCnt += 1


def explode():
    diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    while True: # 4개 이상 연속되는 구슬이 없으면 종료
        x, y = shark
        diffIdx = 0
        cnt = 0
        changeCnt = 1
        trial = 0  # 2회 가야함
        stack = [-1]
        marbleNum = -1

        continuous = [] # 구슬번호 : [(x,y)...]
        while True:
            dx, dy = diff[diffIdx]
            x, y = x + dx, y + dy

            if x < 0 or N <= x or y < 0 or N <= y:
                break

            if graph[x][y] == 0:
                break

            marble = graph[x][y]
            if marble == marbleNum:
                stack.append((x,y))
            else:
                if len(stack) >= 4:
                    continuous.append((marbleNum, stack[:]))
                stack = [(x,y)]
                marbleNum = marble

            cnt += 1

            if cnt == changeCnt:
                diffIdx = (diffIdx + 1) % 4
                cnt = 0
                trial += 1

            if trial == 2:
                trial = 0
                cnt = 0
                changeCnt += 1

        if len(stack) >= 4: # 끝까지 하고 마지막 남아있는 스택 확인
            continuous.append((marbleNum, stack[:]))

        if not continuous:
            break

        # 구슬 폭발
        for num, marbles in continuous:
            cnt = 0
            for x,y in marbles: # 폭발해서 0으로 변경
                graph[x][y] = 0
                cnt += 1

            explosion[num] += cnt # 폭발하는 구슬 카운팅

        # 연속하는 구슬 이동시킴
        move()


def change():
    diff = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x, y = shark
    diffIdx = 0
    cnt = 0
    changeCnt = 1
    trial = 0  # 2회 가야함
    stack = 0
    marbleNum = -1

    continuous = []  # 구슬번호 : [(x,y)...]
    while True:
        dx, dy = diff[diffIdx]
        x, y = x + dx, y + dy

        if x < 0 or N <= x or y < 0 or N <= y:
            break

        if graph[x][y] == 0:
            break

        marble = graph[x][y]
        if marble == marbleNum:
            stack += 1
        else:
            if marbleNum != -1: # 맨처음 상어는 제외
                continuous.append((marbleNum, stack))
            stack = 1
            marbleNum = marble

        cnt += 1

        if cnt == changeCnt:
            diffIdx = (diffIdx + 1) % 4
            cnt = 0
            trial += 1

        if trial == 2:
            trial = 0
            cnt = 0
            changeCnt += 1

    if stack > 0:  # 끝까지 하고 마지막 남아있는 스택 확인
        continuous.append((marbleNum, stack))

    # print(continuous)
    newMarbles = [0]
    for num, cnt in continuous:
        newMarbles.append(cnt)
        newMarbles.append(num)

    # 그대로 다시 넣어준다
    x, y = shark
    diffIdx = 0

    cnt = 0
    changeCnt = 1
    trial = 0  # 2회 가야함
    newMarblesIdx = 1
    length = len(newMarbles)

    while True:
        dx, dy = diff[diffIdx]
        x , y = x + dx, y + dy

        if x < 0 or N <= x or y < 0 or N <= y:
            break

        # 가운데로 당겨서 빈 곳은 0으로
        if newMarblesIdx >= length:
            graph[x][y] = 0
        else:
            graph[x][y] = newMarbles[newMarblesIdx]

        newMarblesIdx += 1
        cnt += 1

        if cnt == changeCnt:
            diffIdx = (diffIdx + 1) % 4
            cnt = 0
            trial += 1

        if trial == 2:
            trial = 0
            cnt = 0
            changeCnt += 1


if __name__ == '__main__':
    N, M = map(int, input().split(' '))
    graph = [list(map(int, input().split(' '))) for _ in range(N)]
    magic = [list(map(int, input().split(' '))) for _ in range(M)]
    shark = ((N+1)//2 - 1, (N+1)//2 - 1)
    explosion = {1 : 0, 2 : 0, 3 : 0}
    for d,s in magic:
        iceAttack(d,s)
        move()
        explode()
        change()

    answer = explosion[1]  + int(explosion[2] * 2) + int(explosion[3] * 3)
    print(answer)