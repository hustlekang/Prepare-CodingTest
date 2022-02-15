#BFS
from collections import deque
m=int(input())
visit=[[False]*m for _ in range(m)]
graph=[]
answerList=[]
queue=deque([])
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]
for _ in range(m):
    graph.append(list(map(int,input())))

for x in range(m):
    for y in range(m):
        if visit[x][y]==False and graph[x][y]==1:
            queue.append([x,y])
            visit[x][y]=True
            cnt=1
            while(queue):
                x1,y1=queue.popleft()
                for dx,dy in zip(directionX,directionY):
                    nx = x1+dx
                    ny = y1+dy
                    if 0<=nx<m and 0<=ny<m and visit[nx][ny]==False and graph[nx][ny]==1:
                        queue.append([nx,ny])
                        visit[nx][ny]=True
                        cnt+=1
            answerList.append(cnt)

answerList.sort()
print(len(answerList))
for answer in answerList:
    print(answer)