N, M, H = map(int, input().split(' '))
maxC = 2*N - 1 # 열 최대
maxR = H + 2 # 행 최대
answer = -1
ladder = [[0] * (2*N - 1) for _ in range(H + 2)]

for _ in range(M): # 사다리 초기화
    r, c = map(int, input().split(' '))
    ladder[r][2*c - 1] = 1

def goDown(position):
    x, y, start = position
    while (x != maxR -1):
        x += 1
        if y + 1 < maxC and ladder[x][y + 1] == 1:  # 오른쪽 사다리로 이동
            y += 2
        elif y - 1 >= 0 and ladder[x][y - 1] == 1:  # 왼쪽 사다리로 이동
            y -= 2

    if start != y: # 시작위치와 마지막 위치 동일하지 않으면
        return False
    return True

def isSuccess():
    success = True
    for y in range(0, maxC, 2):
        if goDown((0, y, y)) == False:
            success = False
            break
    return success

def solution(cnt,maxCnt,x): # x는 탐색 범위 줄이기 위한 행 값
    global answer
    if isSuccess():
        answer = cnt
        return
    if cnt == maxCnt: # maxCnt까지 설치했을 때 안되면 볼 필요 X
        return

    for x in range(x,H+1): # x부터 탐색해서 범위 줄임
        for y in range(1,maxC,2):
            if ladder[x][y] == 0:
                isOk = True
                if y + 2 < maxC and ladder[x][y + 2] == 1:
                    isOk = False
                if y - 2 >= 0 and ladder[x][y - 2] == 1:
                    isOk = False
                if isOk:
                    ladder[x][y] = 1
                    solution(cnt+1,maxCnt,x)
                    ladder[x][y] = 0

if __name__ == '__main__':
    for maxCnt in range(4):
        solution(0,maxCnt,1)
        if answer != -1:
            break
    print(answer)