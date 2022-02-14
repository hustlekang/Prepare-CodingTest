#BFS
from collections import deque
m,n,k=map(int,input().split())
visit=[[False]*n for _ in range(m)]
graph=[[0]*n for _ in range(m)]
queue=deque([])
directionX=[0,0,1,-1]
directionY=[1,-1,0,0]
answer=0
for _ in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

for x in range(m):
    for y in range(n):
        if graph[x][y]==1 and visit[x][y]==False:
            cnt=1
            queue.append([x,y])
            visit[x][y]=True
            while(queue):
                x1,y1=queue.popleft()
                for dx,dy in zip(directionX,directionY):
                    nx=x1+dx
                    ny=y1+dy
                    if 0<=nx<m and 0<=ny<n and visit[nx][ny]==False and graph[nx][ny]==1:
                        queue.append([nx,ny])
                        visit[nx][ny]=True
                        cnt+=1
            answer=max(answer,cnt)
print(answer)