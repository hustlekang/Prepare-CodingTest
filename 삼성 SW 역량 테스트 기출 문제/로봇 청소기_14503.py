from collections import deque

N,M=map(int,input().split())
r,c,d=map(int,input().split())
visit=[[False]*M for _ in range(N)]
direction={
    0:((0,-1),3), # 현재 바라보는 방향 : ( 왼쪽칸의 (dx,dy) , 왼쪽으로 회전 후 바라보는 방향)
    1:((-1,0),0),
    2:((0,1),1),
    3:((1,0),2)
}
back={
    0:(1,0), # 현재 바라보는 방향 : 뒤쪽 칸의 (dx,dy)
    1:(0,-1),
    2:(-1,0),
    3:(0,1)
}
graph=[]
cnt=0
for _ in range(N):
    graph.append(list(map(int,input().split())))

queue=deque([])
queue.append((r,c,d))

while queue:
    x,y,way=queue.popleft()
    if visit[x][y]==False:
        cnt+=1
        visit[x][y]=True
    turnLeft=0
    for trial in range(4):
        dx,dy=direction[way][0]
        newWay=direction[way][1]
        nx=x+dx
        ny=y+dy
        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0 and visit[nx][ny]==False:
            queue.append((nx,ny,newWay))
            break
        else: # 왼쪽이 청소안한 빈칸이 아니면 왼쪽으로 돌기만 한다
            way=newWay
            turnLeft+=1

    if turnLeft==4:
        dx,dy=back[way]
        nx=x+dx
        ny=y+dy
        if graph[nx][ny]==1: #뒤 칸이 벽이면 종료
            break
        else:
            queue.append((nx,ny,way)) #뒤로 후진

print(cnt)