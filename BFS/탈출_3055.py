import sys
from collections import deque

m,n=map(int,input().split())
graph=[]
start=None
target=None
water=[]
visit=[[False]*n for _ in range(m)]
waterVisit=[[False]*n for _ in range(m)]
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]

for i in range(m):
    line=list(sys.stdin.readline().strip())
    if 'S' in line:
        start=[i,line.index('S')]
    if 'D' in line:
        target=[i,line.index('D')]
    if '*' in line:
        temp_water=[]
        for x in range(len(line)):
            if line[x]=='*':
                temp_water.append([i,x])

        for x in temp_water:
            water.append(x)

    graph.append(line)


cnt=1
waterCnt=len(water)
answer="KAKTUS"
graph[start[0]][start[1]]='.'
queue = deque([[start[0],start[1],0]])
waterQueue = deque(water)

visit[start[0]][start[1]]=True
for i in water:
    waterVisit[i[0]][i[1]]=True

while queue:
    waterPop=[]
    for _ in range(waterCnt):
        waterPop.append(waterQueue.pop())
    waterCnt=0
    #물 먼저 확장시키고
    for water in waterPop:
        for dx,dy in zip(directionX,directionY):
            nx= water[0]+dx
            ny= water[1]+dy
            if 0<=nx<m and 0<=ny<n and waterVisit[nx][ny]==False and graph[nx][ny]=='.':
                waterQueue.append([nx,ny])
                waterVisit[nx][ny]=True
                graph[nx][ny]="*"
                waterCnt+=1
    #고슴도치 이동시키자

    animalPop=[]
    for _ in range(cnt):
        v=queue.pop()
        if v[0]==target[0] and v[1]==target[1]:
            answer=v[2]
            queue.clear()
            break

        animalPop.append(v)

    cnt=0

    for animal in animalPop:
        for dx,dy in zip(directionX,directionY):
            nx = animal[0]+dx
            ny = animal[1]+dy
            if 0<=nx<m and 0<=ny<n and visit[nx][ny]==False and (graph[nx][ny]=='.' or graph[nx][ny]=='D'):
                queue.append([nx,ny,animal[2]+1])
                visit[nx][ny]=True
                cnt+=1

print(answer)