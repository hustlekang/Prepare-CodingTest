from math import floor

# 시작 (x,y)에서 3방향으로 계속 번진 좌표들을 담은 집합을 반환
def spread(x,y, nextBlock, noWall, level, willUpdateBlock):
    willUpdateBlock.add((x,y,level))

    if level == 1 : return

    for i in range(3): # 진행 방향 3가지
        dx, dy = nextBlock[i]
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C: # 정상 범위에 있을 때
            canSpread = True
            for block1, block2 in noWall[i]:
                dx1, dy1 = block1
                dx2, dy2 = block2
                if ((x + dx1, y + dy1), (x + dx2, y + dy2)) in walls: # 벽이 있으면 못감
                    canSpread = False
                    break

            if not canSpread: continue
            spread(nx, ny, nextBlock, noWall, level -1, willUpdateBlock)


def heat():
    heaterInfo = {
        1 : { # 오른쪽으로
            'firstDif' : (0, 1),
            'nextBlock' : [(-1,1), (0,1), (1,1)], # 오른쪽위, 오른쪽, 오른쪽아래
            'noWall' : [
                [((0,0),(-1,0)), ((-1,0),(-1,1))],
                [((0,0),(0,1))],
                [((0,0),(1,0)), ((1,0),(1,1))]
            ]
        },
        2 : { # 왼쪽으로
            'firstDif' : (0,-1),
            'nextBlock' : [(-1,-1), (0,-1), (1,-1)], # 왼쪽위, 왼쪽, 왼쪽아래
            'noWall' : [
                [((0,0),(-1,0)), ((-1,0),(-1,-1))],
                [((0,0),(0,-1))],
                [((0,0),(1,0)), ((1,0),(1,-1))]
            ]
        },
        3 : { # 위로
            'firstDif' : (-1,0),
            'nextBlock' : [(-1,-1), (-1,0), (-1,1)], # 위왼쪽, 위, 위오른쪽
            'noWall' : [
                [((0,0),(0,-1)), ((0,-1),(-1,-1))],
                [((0,0),(-1,0))],
                [((0,0),(0,1)), ((0,1),(-1,1))]
            ]
        },
        4 : { # 아래로
            'firstDif': (1,0),
            'nextBlock': [(1,0), (1,-1), (1,1)], # 아래, 아래왼쪽, 아래오른쪽
            'noWall': [
                [((0,0),(1,0))],
                [((0,-1),(0,0)), ((0,-1),(1,-1))],
                [((0,0),(0,1)), ((0,1),(1,1))]
            ]
        }
    }

    for x,y,direction in heaters: #(x, y, 히터종류)
        dx, dy = heaterInfo[direction]['firstDif']
        startX, startY = x + dx, y + dy
        willUpdateBlock = set()

        spread(startX,
               startY,
               heaterInfo[direction]['nextBlock'],
               heaterInfo[direction]['noWall'],
               5,
               willUpdateBlock
        )
        # 모든 좌표들 온도 업데이트
        for x, y, temperature in willUpdateBlock:
            graph[x][y] += temperature


# 모든 히터를 가동해서 온도 업데이트하는 함수
def adjustment():
    willAdjArr = []
    for x in range(R):
        for y in range(C):
            for dx,dy in zip([0,0,-1,1],[1,-1,0,0]):
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and ((x,y),(nx,ny)) not in walls: # 정상 범위이고 벽이 없을 때만
                    t = floor((graph[x][y] - graph[nx][ny]) / 4)
                    if t > 0: # x,y에서 nx,ny로 줄 수 있으면
                        willAdjArr.append((x, y, nx, ny, t))

    for fromX, fromY, toX, toY, t in willAdjArr:
        graph[fromX][fromY] -= t
        graph[toX][toY] += t


# 테두리 온도 -1 하는 함수
def outlineDecrease():
    for i in range(C): # 맨위, 맨아래
        if graph[0][i] > 0:
            graph[0][i] -= 1
        if graph[-1][i] > 0:
            graph[-1][i] -= 1

    if R < 3: return

    for i in range(1, R - 1): # 맨위와 맨아래 사이에 있는 맨왼쪽, 맨 오른쪽
        if graph[i][0] > 0:
            graph[i][0] -= 1
        if graph[i][-1] > 0:
            graph[i][-1] -= 1


if __name__ == '__main__':
    R, C, K = map(int, input().split(' '))
    heaterNum= {1,2,3,4}
    heaters = [] # (x,y,바람방향)
    target = [] # K도 이상 되어야하는 좌표
    graph = []

    for i in range(R):
        row = list(map(int, input().split(' ')))
        graph.append(row)

        for j in range(C):
            if row[j] in heaterNum:
                heaters.append((i, j, row[j]))
                row[j] = 0 # 온도는 0으로 변경
            elif row[j] == 5:
                target.append((i, j))
                row[j] = 0  # 온도는 0으로 변경

    W = int(input())
    walls = set() # (x,y) 와 (a,b) 사이에 벽은 ((x,y),(a,b))로 표현

    for _ in range(W):
        x, y, t = map(int, input().split(' '))
        x -= 1 # 첫행을 0 으로
        y -= 1 # 첫열을 0으로

        if t == 0:
            walls.add(((x, y), (x - 1, y))) # ((x,y),(a,b)) 두 점의 순서 바뀔 수도 있으니 바꾼것도 add
            walls.add(((x - 1, y), (x, y))) # ((a,b),(x,y))
        else:
            walls.add(((x, y), (x, y + 1)))
            walls.add(((x, y + 1), (x, y)))

    chocolate = 0
    while True: # 초콜릿이 101이면 종료 or target칸들이 K도 이상이면 종료
        heat() # 온풍기 틀고 온도 상승시키고
        adjustment() # 모든칸 온도 조절
        outlineDecrease() # 테두리 온도 -1
        chocolate += 1 # 초콜릿 먹는다

        isOk = True
        for x, y in target:
            if graph[x][y] < K:
                isOk = False
                break

        if isOk or chocolate == 101: break

    print(chocolate)