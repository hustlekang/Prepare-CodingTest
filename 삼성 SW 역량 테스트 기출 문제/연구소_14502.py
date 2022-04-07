from collections import deque
from copy import deepcopy
n,m=map(int,input().split())
answer=0
graph=[]
emtpy=[]
safeZone=-3 #나중에 벽 3개 세울꺼니까 -3에서 시작
virus=[]
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]
for i in range(n):
    line=list(map(int,input().split()))
    for j in range(len(line)):
        if line[j]==0:
            emtpy.append((i,j))
            safeZone+=1
        elif line[j]==2:
            virus.append((i,j))
    graph.append(line)

##조합
l = emtpy
N = len(l)
R = 3
result = []

def combination(idx, list):
    if len(list) == R:
        result.append(list[:])
        return
    for i in range(idx, N):
        combination(i+1,list+[l[i]])

combination(0,[])

for combi in result:
    newVirus = 0
    visit=[[False]*m for _ in range(n)]
    buildGraph=deepcopy(graph)
    for xy in combi: # 벽 3개 세우고
        buildGraph[xy[0]][xy[1]]=1
    for xy in virus: # 큐에 넣고 시작하는 바이러스 좌표 방문처리
        visit[xy[0]][xy[1]]=True

    queue = deque(virus)
    while queue:
        x,y=queue.popleft()
        for dx,dy in zip(directionX,directionY):
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==False and buildGraph[nx][ny]==0:
                visit[nx][ny]=True
                queue.append((nx,ny))
                newVirus+=1

    answer=max(safeZone-newVirus,answer)

print(answer)