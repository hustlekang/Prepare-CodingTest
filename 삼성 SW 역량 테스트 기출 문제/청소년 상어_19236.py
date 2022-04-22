from collections import deque
from copy import deepcopy

queue=deque([])
graph_init=[]

fishLocation_init={} # 키는 물고기번호 값은 [x,y]
differByWay={ # 방향에 따른 dx,dy
    1:(-1,0),
    2:(-1,-1),
    3:(0,-1),
    4:(1,-1),
    5:(1,0),
    6:(1,1),
    7:(0,1),
    8:(-1,1)
}
for i in range(4):
    temp=[]
    line=list(map(int, input().split()))
    for j in range(0,7,2):
        temp.append(line[j:j+2])
        fishLocation_init[line[j]]=[i,j//2]
    graph_init.append(temp)

answer=graph_init[0][0][0] # (0,0)에 위치한 물고기 먹고시작
shark=[-1,graph_init[0][0][1]]
graph_init[0][0]=shark
fishLocation_init.pop(list(fishLocation_init.keys())[0]) # 먹힌 물고기 제거
fishLocation_init[-1]=[0,0] # 상어 위치 기록

queue.append((answer,graph_init,fishLocation_init)) # (지금까지 먹은 번호합,그래프,물고기 위치)

while queue:
    sumOfSharkEat,graph,fishLocation=queue.popleft()

    # 물고기부터 이동
    for fish in range(1,17):
        if fish in fishLocation.keys(): # 1~16번 중 현재 존재하는 물고기만 이동
            x,y=fishLocation[fish] # graph에서 물고기의 좌표
            way=graph[x][y][1] # 물고기의 방향
            turnLeft=0  #7번 돌아도 안되면 안되는거

            while True:
                dx,dy=differByWay[way]
                nx=x+dx
                ny=y+dy

                if 0<=nx<4 and 0<=ny<4 and graph[nx][ny][0] !=-1: # 정상 범위이고 상어만 없으면 이동가능
                    if graph[nx][ny]==[0,0]: # 빈칸일때
                        graph[nx][ny]=[fish,way] # 물고기 이동
                        graph[x][y]=[0,0] # 원래 있던 자리 빈칸으로 초기화
                        fishLocation[fish]=[nx,ny] # 물고기 위치 업데이트
                    else: # 물고기가 있으면
                        otherFish=graph[nx][ny]
                        temp=otherFish
                        graph[nx][ny]=[fish,way] # 새로운곳으로 물고기 이동
                        graph[x][y]=temp # 원래 자리에 바꿔치기
                        fishLocation[fish]=[nx, ny] # 물고기 위치 업데이트
                        fishLocation[temp[0]]=[x,y] # 물고기 위치 업데이트

                    break  # 이동을 마쳤으면 while문 종료

                else: # 이동할 수 없을때는 방향을 바꾼다
                    way+=1
                    if way>8:
                        way-=8
                    turnLeft+=1

                if turnLeft==8: # 결국 원래 방향까지 오면 이동 불가 while문 탈출
                    break

    # 상어 이동 시작
    x,y = fishLocation[-1]
    dx,dy = differByWay[graph[x][y][1]]
    eatableFishes=[]

    while True:
        x+=dx
        y+=dy
        if  0<=x<4 and 0<=y<4:
            if graph[x][y]!=[0,0]: #빈 공간은 먹을수 없다
                eatableFishes.append(graph[x][y])
        else:
            break

    if len(eatableFishes)==0:
        answer=max(sumOfSharkEat,answer)

    else:
        #물고기를 먹는다
        for target in eatableFishes: # [번호,방향]
            graph_new=deepcopy(graph)
            fishLocation_new=deepcopy(fishLocation)

            target_x,target_y = fishLocation_new[target[0]] # 물고기의 좌표
            graph_new[target_x][target_y]=[-1,target[1]] # 상어를 이동시키고
            graph_new[fishLocation_new[-1][0]][fishLocation_new[-1][1]]=[0,0] # 상어 있던 자리는 빈공간으로
            fishLocation_new[-1]=[target_x,target_y] # 상어 위치 업데이트
            fishLocation_new.pop(target[0]) # 물고기 위치는 제거해준다

            queue.append((sumOfSharkEat+target[0],graph_new,fishLocation_new))

print(answer)