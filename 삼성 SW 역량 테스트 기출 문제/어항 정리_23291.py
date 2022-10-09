# 1차원 배열 fishbowls에서 물고기 가장 적은거 찾아서 한마리 추가하는 함수
def addFish():
    global fishbowls
    minCnt = 100000
    minBowlIdx = []
    for i in range(len(fishbowls)):
        if fishbowls[i] < minCnt:
            minCnt = fishbowls[i]
            minBowlIdx = [i]
        elif fishbowls[i] == minCnt:
            minBowlIdx.append(i)

    for i in minBowlIdx:
        fishbowls[i] += 1

# 맨 왼쪽에 있는 어항 위로 올려서 2층짜리 2차원 배열로 만드는 함수, 빈 공간은 -1
def leftOn():
    global fishbowls
    top = [fishbowls[0]] + [-1] * (len(fishbowls) - 2)
    fishbowls = [top,fishbowls[1:]]

# 2차원 배열 90도 돌린거 리턴하는 함수
def rotate(matrix):
    n = len(matrix)
    if n == 1: # [x]
        return matrix

    m = len(matrix[0])
    newMatrix = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            newMatrix[j][n-1-i] = matrix[i][j]

    return newMatrix

# 맨 왼쪽부터 공중부양해서 90도 돌려서 위에 얹히는 함수
def jumpUp():
    global fishbowls
    jumpCnt = [1] # 앞에서부터 가로로 1개 면적, 2개면적, 2개면적, 3개면적, 3개면적 ...
    for i in range(2, 11):
        jumpCnt.append(i)
        jumpCnt.append(i)

    for cnt in jumpCnt:
        if len(fishbowls) > len(fishbowls[0]) - cnt: # 90도 돌려서 올리는게 맨 아래층보다 넓으면 불가능
                return

        block = [row[:cnt] for row in fishbowls]
        rotatedBlock = rotate(block)

        bottom = [row[cnt:] for row in fishbowls][-1] # 맨 아랫 부분

        for i in range(len(rotatedBlock)):
            for _ in range(len(bottom)-len(rotatedBlock[-1])):
                rotatedBlock[i].append(-1)

        newFishbowls = []
        for row in rotatedBlock:
            newFishbowls.append(row)
        newFishbowls.append(bottom)

        fishbowls = newFishbowls

# 모든 물고기 이동시키는 함수
def moveFish():
    global fishbowls
    n = len(fishbowls)
    m = len(fishbowls[0])

    updateInfo = set() # (fromX,fromY,toX,toY,cnt)

    for x in range(n):
        for y in range(m):
            if fishbowls[x][y] == -1: continue

            cnt = fishbowls[x][y]
            for dx, dy in zip([0,0,1,-1],[1,-1,0,0]):
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and fishbowls[nx][ny] != -1:
                    otherCnt = fishbowls[nx][ny]
                    d = abs(cnt - otherCnt) // 5
                    if d > 0:
                        if cnt > otherCnt:
                            updateInfo.add((x,y,nx,ny,d))
                        else:
                            updateInfo.add((nx,ny,x,y,d))

    for fromX,fromY,toX,toY,cnt in updateInfo:
        fishbowls[fromX][fromY] -= cnt
        fishbowls[toX][toY] += cnt

# 2차원 어항들 1차원 배열로 만드는 함수
def makeArr1d():
    global fishbowls
    n = len(fishbowls)
    m = len(fishbowls[0])
    arr_1d = []

    for i in range(m):
        for j in range(n):
            if fishbowls[n-1-j][i] == -1:
                continue
            arr_1d.append(fishbowls[n-1-j][i])

    fishbowls = arr_1d

# 두번째 공중부양 로직 함수
def jumpUp2():
    global fishbowls
    n = len(fishbowls) // 2
    upside = fishbowls[:n][::-1]
    downside = fishbowls[n:]

    fishbowls = [upside,downside] # 절반 180도 돌려서 처리해주고

    leftside = [row[:n//2] for row in fishbowls]
    rightside = [row[n//2:] for row in fishbowls]

    newFishbowls = [] # 한번더 처리한 결과
    rotated180 = rotate(rotate(leftside))

    # [[x],[y]] 2번 돌리면 [[y],[x]] 나와야 하는데 [[y,x]]나와서 이럴때만 처리
    if len(rotated180) == 1 and len(rotated180[0]) == 2:
        rotated180 = [[rotated180[0][0]], [rotated180[0][1]]]

    for row in rotated180:
        newFishbowls.append(row)
    for row in rightside:
        newFishbowls.append(row)

    fishbowls = newFishbowls

if __name__ == '__main__':
    trial = 0
    N, K = map(int, input().split(' '))
    fishbowls = list(map(int,input().split(' ')))

    while abs(max(fishbowls) - min(fishbowls)) > K:
        trial += 1
        addFish()
        leftOn()
        jumpUp()
        moveFish()
        makeArr1d()
        jumpUp2()
        moveFish()
        makeArr1d()

    print(trial)