from copy import deepcopy
from collections import deque

answer=0
R,C,T=map(int,input().split())
graph=[]
airConditioner=[] # 공기청정기 x값
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]
for i in range(R):
    row=list(map(int,input().split()))
    if row[0]==-1:
        airConditioner.append(i)
    graph.append(row)

for _ in range(T):
    beforeSpread = deepcopy(graph)
    afterSpread = [[0]*C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if beforeSpread[x][y]>=5:
                spreadAreas=[] # (x,y,먼지량)
                total=beforeSpread[x][y]
                amount=total
                for dx,dy in zip(directionX,directionY):
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<R and 0<=ny<C and (nx,ny) not in [(airConditioner[0],0),(airConditioner[1],0)]:
                        spreadAreas.append((nx,ny,total//5))
                        amount-=total//5

                spreadAreas.append((x,y,amount))
                for spreadArea in spreadAreas: # 먼지가 이동된 영역들
                    r,c,dust=spreadArea
                    afterSpread[r][c]+=dust

            else:
                afterSpread[x][y]+=beforeSpread[x][y]

    #위에 반시계
    # 선언을 한번에 해야됨, 한 테두리씩 시프트 시키면 변하니까
    bottom = deque(afterSpread[airConditioner[0]])
    top = deque(afterSpread[0])
    right = deque([line[-1] for line in afterSpread[:airConditioner[0] + 1]])
    left = deque([line[0] for line in afterSpread[:airConditioner[0] + 1]])

    # 맨 아래 가로 줄 조작
    bottom.pop()
    bottom.popleft()
    bottom.appendleft(0)
    bottom.appendleft(-1)

    #맨 위 가로줄 조작
    top.popleft()
    top.append(afterSpread[1][-1])

    # 오른쪽 세로줄 조작
    right.popleft()
    right.append(afterSpread[airConditioner[0]][-2])

    # 왼쪽 세로줄 조작
    left.appendleft(afterSpread[0][1])
    left.pop()
    left.pop()
    left.append(-1)

    #적용
    afterSpread[airConditioner[0]] = list(bottom)
    afterSpread[0] = list(top)
    for i in range(len(right)):
        afterSpread[i][-1]=right[i]
    for i in range(len(left)):
        afterSpread[i][0]=left[i]

    # 아래 시계 방향 회전
    # 선언부터
    counterClock_top = deque(afterSpread[airConditioner[1]])
    counterClock_bottom = deque(afterSpread[-1])
    counterClock_right = deque([line[-1] for line in afterSpread[airConditioner[1]:]])
    counterClock_left = deque([line[0] for line in afterSpread[airConditioner[1]:]])

    # 위에 가로줄 조작
    counterClock_top.pop()
    counterClock_top.popleft()
    counterClock_top.appendleft(0)
    counterClock_top.appendleft(-1)

    # 아래 가로줄 조작
    counterClock_bottom.popleft()
    counterClock_bottom.append(afterSpread[-2][-1])

    # 왼쪽 세로줄 조작
    counterClock_left.popleft()
    counterClock_left.append(afterSpread[-1][1])
    counterClock_left.popleft()
    counterClock_left.appendleft(-1)

    # 오른쪽 세로줄 조작
    counterClock_right.pop()
    counterClock_right.appendleft(afterSpread[airConditioner[1]][-2])

    #적용
    afterSpread[airConditioner[1]]=list(counterClock_top)
    afterSpread[-1]=list(counterClock_bottom)
    for i in range(len(counterClock_right)):
        afterSpread[i+airConditioner[1]][-1]=counterClock_right[i]
    for i in range(len(counterClock_left)):
        afterSpread[i+airConditioner[1]][0]=counterClock_left[i]

    graph=afterSpread #그래프를 1초후로 갱신
# 공기청정기 위치 -1 sum()에 방해되니 제거
graph[airConditioner[0]][0]=0
graph[airConditioner[1]][0]=0

for row in graph:
    answer+=sum(row)

print(answer)