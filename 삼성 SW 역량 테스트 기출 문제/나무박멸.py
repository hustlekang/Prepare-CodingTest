# 코드트리
# 22년 상반기 오후 2번

def grow():
    global N, trees

    for x,y in trees:
        adjacent = 0
        for dx, dy in zip([0,0,1,-1], [1,-1,0,0]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) in trees:
                adjacent += 1

        graph[x][y] += adjacent


def breede():
    global N, trees, deadZone, graph
    updateTrees = set()
    updateInfo = []

    for x,y in trees:
        cnt = 0
        adjacentPoint = []
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0 and not deadZone[nx][ny]:
                cnt += 1
                adjacentPoint.append((nx, ny))

        if cnt == 0:
            continue

        quantity = graph[x][y] // cnt
        #!!!!!!!!!!! 0 이면 나무가 새로 안생기는건데 tree에 업데이트해서 계속 틀렸었다...
        # 현재 칸에 있는 나무가 1이고 주변에 빈칸이 4면 1/4이어서 번식은 가능하지만 그 수가 0 이므로 불가능함
        if quantity == 0:
            continue

        for ax,ay in adjacentPoint:
            updateInfo.append((ax,ay,quantity))

    # 번식은 모든 정보를 얻고 한번에 해야 아직 탐색 안한 나무에 영향을 안준다
    for x, y, q in updateInfo:
        graph[x][y] += q
        trees.add((x,y))

    trees |= updateTrees


def makeDeadZone(year):
    global N, K, graph, deadZone, deadZoneExpire, trees
    maxKill = 0
    point = (4, 4) # 제초제 뿌릴 위치
    allPoints = [] # 제초제 전파되는 모든 위치

    for x,y in trees:
        kill = graph[x][y]
        tempAllPoints = []
        for dx, dy in zip ([1,-1,1,-1],[1,-1,-1,1]):
            t = 1 # 확산 횟수
            nx, ny = x + dx, y + dy

            if nx < 0 or N <= nx or ny < 0 or N <= ny:
                continue

            tempAllPoints.append((nx, ny))

            if graph[nx][ny] == -1 or graph[nx][ny] == 0:
                continue

            kill += graph[nx][ny] # 나무가 있을 때만 더해지지

            while t < K:
                t += 1
                nx += dx
                ny += dy
                if nx < 0 or N <= nx or ny < 0 or N <= ny:
                    break

                tempAllPoints.append((nx, ny))
                if graph[nx][ny] == -1 or graph[nx][ny] == 0:
                    break
                kill += graph[nx][ny]  # 나무가 있을 때만 더해지지

        if maxKill < kill:
            point = (x,y)
            allPoints = tempAllPoints
            maxKill = kill

        elif maxKill == kill:
            if x < point[0]:
                point = (x, y)
                allPoints = tempAllPoints

            elif x == point[0] and y < point[1]:
                point = (x, y)
                allPoints = tempAllPoints

    allPoints.append(point)

    for x,y in allPoints:
        deadZone[x][y] = True
        deadZoneExpire[x][y] = year + C

        if (x,y) in trees:
            trees.remove((x,y))
            graph[x][y] = 0 # 빈 곳으로 만들어야지

    return maxKill


def updateDeadZone(year):
    global N, deadZone, deadZoneExpire
    for i in range(N):
        for j in range(N):
            if deadZone[i][j] and deadZoneExpire[i][j] == year:
                deadZone[i][j] = False
                deadZoneExpire[i][j] = 0


def process():
    global M
    cnt = 0

    for year in range(1 , M + 1):
        grow()
        breede()
        cnt += makeDeadZone(year)
        updateDeadZone(year)

    return cnt


if __name__ == '__main__':
    N, M, K, C = map(int ,input().split())
    graph = []
    trees = set()
    deadZone = [
        [False] * N for _ in range(N)
    ]
    deadZoneExpire = [
        [0] * N for _ in range(N)
    ]

    for i in range(N):
        row = list(map(int, input().split()))
        graph.append(row)
        for j in range(N):
            if row[j] > 0: # 나무가 있을 떄
                trees.add((i,j))

    answer = process()
    print(answer)