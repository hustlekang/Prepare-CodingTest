#BFS
from collections import deque
m,n,k=map(int,input().split())
graph=[[0]*n for _ in range(m)]
visit=[[False]*n for _ in range(m)]
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]
answerList=[]
queue = deque([])
for _ in range(k):
    y1,x1,y2,x2=map(int,input().split())
    for nx in range(x1,x2):
        for ny in range(y1,y2):
            graph[nx][ny]=1

queue = deque([])
for x in range(m):
    for y in range(n):
        if not visit[x][y] and graph[x][y]==0:
            cnt=1
            queue.append([x,y])
            visit[x][y]=True
            while (queue):
                a,b=queue.popleft()
                for dx,dy in zip(directionX,directionY):
                    nx=a+dx
                    ny=b+dy
                    if 0<=nx<m and 0<=ny<n and visit[nx][ny]==False and graph[nx][ny]==0:
                        queue.append([nx,ny])
                        visit[nx][ny]=True
                        cnt+=1
            answerList.append(cnt)

answerList.sort()
print(len(answerList))
for answer in answerList:
    print(answer,end=" ")

