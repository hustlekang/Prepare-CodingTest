from copy import deepcopy

def xyToKey(x,y):
    return str(x) + str(y)

# 이동시킨 물고기 딕셔너리를 반환
def moveFishes():
    direction = {
        1: (0, -1),
        2: (-1, -1),
        3: (-1, 0),
        4: (-1, 1),
        5: (0, 1),
        6: (1, 1),
        7: (1, 0),
        8: (1, -1)
    }

    newFishes = {}
    for i in range(4):
        for j in range(4):
            key = str(i) + str(j)
            newFishes[key] = []

    for key in fishes.keys():
        x, y = int(key[0]), int(key[1])
        for fish in fishes[key]: # fish = 방향
            for _ in range(8):
                dx, dy = direction[fish]
                nx, ny = x + dx, y + dy
                if (nx,ny) not in scent and (nx,ny) != shark and 0 <= nx < 4 and 0 <= ny < 4:
                    newFishes[str(nx)+str(ny)].append(fish)
                    break

                fish -= 1
                if fish == 0:
                    fish = 8

            else: # 이동불가인 물고기 처리
                newFishes[key].append(fish)

    return newFishes

# 상어 이동 로직 처리 후 이동한 상어의 좌표 반환
def sharkMove(x,y, trial):
    direction = {
        1 : (-1,0),
        2 : (0,-1),
        3 : (1,0),
        4 : (0,1)
    }
    way = '000'
    maxCnt = -1

    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                dx1, dy1 = direction[i]
                dx2, dy2 = direction[j]
                dx3, dy3 = direction[k]
                cnt = 0

                # 1회 이동
                nx,ny = x + dx1, y + dy1
                if nx < 0 or 3 < nx or ny < 0 or 3 < ny:
                    continue
                cnt += len(fishes[xyToKey(nx, ny)])
                # 1회 이동한 좌표를 기억해야 3번째 이동 때 물고기 중복으로 안먹음
                x1,y1 = nx, ny

                # 2회 이동
                nx, ny = nx + dx2, ny + dy2
                if nx < 0 or 3 < nx or ny < 0 or 3 < ny:
                    continue
                cnt += len(fishes[xyToKey(nx, ny)])

                # 3회 이동
                nx, ny = nx + dx3, ny + dy3
                if nx < 0 or 3 < nx or ny < 0 or 3 < ny:
                    continue
                if (nx,ny) != (x1,y1): # 처음 이동했을 때 먹은거는 제외
                    cnt += len(fishes[xyToKey(nx, ny)])

                newWay = '{}{}{}'.format(i, j, k)
                if maxCnt < cnt:
                    way = newWay
                    maxCnt = cnt
                elif maxCnt == cnt and int(newWay) < int(way):
                    way = newWay

    # 설정한 방향대로 상어 이동시키며 먹은 물고기 제거하고 냄새 남김
    sharkX,sharkY = x, y
    for d in way:
        dx, dy = direction[int(d)]
        sharkX, sharkY = sharkX + dx, sharkY + dy
        if fishes[xyToKey(sharkX,sharkY)]: # 물고기가 있을 시
            fishes[xyToKey(sharkX, sharkY)] = []
            scent.add((sharkX, sharkY))
            scentExpire[(sharkX, sharkY)] = trial

    return (sharkX, sharkY)

def copyFishes(origin):
    for key in origin.keys():
        for each in origin[key]:
            fishes[key].append(each)

if __name__ == '__main__':
    M, S = map(int, input().split(' '))
    fishes = {}
    scent = set()
    scentExpire = {} # 좌표별 물고기 냄새의 소멸 시기
    for i in range(4):
        for j in range(4):
            key = str(i) + str(j)
            fishes[key] = []
            scentExpire[(i,j)] = 1000

    for _ in range(M):
        x, y, d = map(int, input().split(' '))
        key = str(x - 1) + str(y - 1)
        fishes[key].append(d)

    shark = tuple(map(lambda x:int(x)-1, input().split(' ')))

    # S회 마법 실행
    for trial in range(1, S + 1):
        initFishes = deepcopy(fishes)
        fishes = moveFishes() # 모든 물고기 이동
        shark = sharkMove(shark[0], shark[1], trial) # 상어 이동

        if trial >= 3: # 3트부터는 냄새 소멸 체크
            for key in scentExpire:
                if trial - 2 == scentExpire[key]:
                    scentExpire[key] = 1000
                    scent.discard(key)

        copyFishes(initFishes)

    answer = 0
    for key in fishes:
        answer += len(fishes[key])

    print(answer)