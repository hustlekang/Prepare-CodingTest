# 얼음을 녹일 때 녹일 위치를 저장했다가 한번에 녹여야 하는데 탐색 도중 녹여서 틀림
# 최대 연결 얼음 크기 구할 때 초기값 1로 뒀다가 틀림 , 남아있는 얼음이 없으면 0인데 초기값을 1로 둬서 1나와서 틀림
#pypy
from collections import deque

def spin(list): #90도 시계방향으로 회전
    newList=[]
    for i in range(len(list)):
        newList.append([j[i] for j in list[::-1]])
    return newList

def rotate(graph,n): # rotate(돌릴 그래프, 2**l 로 격자를 나눌 l)
    graphL=len(graph)
    blockL=int(graphL/(2**n))
    idx=[]
    for k in range(blockL):
        idx.append(k * (2 ** n))
    idx.append(graphL)

    for i in range(blockL):
        # print(idx[i],idx[i+1])
        for j in range(blockL):
            # x는 idx[i]:idx[i+1] 까지, y는 idx[j]:idx[j + 1]
            spinned=spin([cut[idx[j]:idx[j + 1]] for cut in graph[idx[i]:idx[i+1]]])
            for col in range(idx[i],idx[i+1]):
                for row in range(idx[j],idx[j + 1]):
                    graph[col][row]=spinned[col-idx[i]][row-idx[j]]
    return graph

total=0
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]
N,Q=map(int,input().split())
graph=[]
for _ in range(2**N):
    graph.append(list(map(int,input().split())))
L=list(map(int,input().split()))

for l in L:
    graph=rotate(graph,l)
    willMelt=[] #탐색하면서 바로바로 녹여버리면 1인 경우에 0이 되니까 오류가 생김, 위치 저장했다가 한번에 해야함
    for x in range(2**N):
        for y in range(2**N):
            if graph[x][y]>0:
                cnt=0
                for dx,dy in zip(directionX,directionY):
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<2**N and 0<=ny<2**N and graph[nx][ny]>0:
                        cnt+=1

                if cnt<3:
                    willMelt.append((x,y))

    for ice in willMelt:
        graph[ice[0]][ice[1]]-=1

for line in graph:
    total+=sum(line)

visit=[[False]*(2**N) for _ in range(2**N)]
queue=deque([])
biggest=0
for x in range(2 ** N):
    for y in range(2 ** N):
        connected = 0  # 얼음이 없으면 일단 0
        if graph[x][y]>0 and visit[x][y]==False:
            connected=1 # 한개라도 있으면 1
            visit[x][y]=True
            queue.append((x,y))

        while queue:
            x1,y1=queue.popleft()
            for dx,dy in zip(directionX,directionY):
                nx = x1 + dx
                ny = y1 + dy
                if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and graph[nx][ny] > 0 and visit[nx][ny]==False:
                    queue.append((nx,ny))
                    visit[nx][ny]=True
                    connected+=1

        biggest=max(biggest,connected)

print(total)
print(biggest)