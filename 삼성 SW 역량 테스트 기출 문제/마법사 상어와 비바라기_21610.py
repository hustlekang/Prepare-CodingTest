n,m=map(int,input().split())
answer=0
graph=[]
moving=[]
cloudPosition=[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for _ in range(n):
    graph.append(list(map(int,input().split())))
for _ in range(m):
    moving.append(list(map(int,input().split())))

commandDirection={1:(0,-1),2:(-1,-1),3:(-1,0),4:(-1,1),5:(0,1),6:(1,1),7:(1,0),8:(1,-1)}

for moveInfo in moving:
    dx,dy=commandDirection[moveInfo[0]] #구름의 이동 증가량
    cnt=moveInfo[1] #구름 이동시킬 칸수
    isExpire=[[False]*n for _ in range(n)] #구름이 소멸된 위치 기록

    for i in range(len(cloudPosition)): # 모든 구름을 이동시킨다
        x,y=cloudPosition[i]
        nx=(x+dx*cnt)%n
        ny=(y+dy*cnt)%n
        cloudPosition[i]=(nx,ny)

    for cloud in cloudPosition: #구름 위치에 물량 1증가
        graph[cloud[0]][cloud[1]]+=1
        isExpire[cloud[0]][cloud[1]]=True

    for block in cloudPosition: #물 복사 버그 시전
        x=block[0]
        y=block[1]
        digonalCnt = 0
        for direction in [commandDirection[i] for i in range(2,9,2)]:
            nx=x+direction[0]
            ny=y+direction[1]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>0:
                digonalCnt+=1

        graph[x][y]+=digonalCnt # 대각선에 물이 있는 칸수만큼 증가

    cloudPosition.clear() #구름 위치 초기화 해주고 다시 세팅
    for i in range(n):
        for j in range(n):
            if isExpire[i][j]==False and graph[i][j]>=2:
                graph[i][j]-=2
                cloudPosition.append((i,j))

for line in graph:
    answer+=sum(line)

print(answer)