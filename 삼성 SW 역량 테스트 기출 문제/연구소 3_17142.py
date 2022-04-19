# PyPy3
from collections import deque
from copy import deepcopy

N,M=map(int,input().split())
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]
graph=[]
virus=[]
min_sec=10**10
answer=0

for i in range(N):
    row=list(map(int,input().split()))
    for j in range(N):
        if row[j]==2:
            virus.append((i,j))
    graph.append(row)

# 조합
l = virus
n = len(l)
r = M
result = []
def combination(idx, list):
    if len(list) == r:
        result.append(list[:])
        return

    for i in range(idx, n):
        combination(i+1,list+[l[i]])

combination(0, [])

for activatedViruses in result:
    unActivatedViruses=list(set(virus)-set(activatedViruses))
    labotory = deepcopy(graph)
    visit = [[False] * N for _ in range(N)]
    queue = deque([])
    done_sec = 0
    cantSpreadAll = False

    for activatedVirus in activatedViruses: # 활성바이러스 큐에 넣어주고 방문처리
        visit[activatedVirus[0]][activatedVirus[1]]=True
        labotory[activatedVirus[0]][activatedVirus[1]]=0
        queue.append((activatedVirus[0],activatedVirus[1],0))

    for unActivatedVirus in unActivatedViruses: #비활성 바이러스 -1로 표기
        labotory[unActivatedVirus[0]][unActivatedVirus[1]]=-1

    while queue:
        x,y,sec=queue.popleft()
        for dx,dy in zip(directionX,directionY):
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==False and (labotory[nx][ny]==0 or labotory[nx][ny]==-1 ):
                visit[nx][ny]=True
                queue.append((nx,ny,sec+1))
                if labotory[nx][ny]==0: # 빈 공간에 확산시킬 때만 시간 갱신
                    done_sec = sec+1

    for i in range(N):
        for j in range(N):
            if visit[i][j]==False and labotory[i][j]==0: #방문 안헀는데 빈공간이면 모든 곳에 확산 불가능
                cantSpreadAll=True
                break
        if cantSpreadAll:
            break

    if not cantSpreadAll: # 모두 퍼질 수 있을때만 최소시간 갱신
        min_sec=min(min_sec,done_sec)

if min_sec==10**10:
    answer=-1
else:
    answer=min_sec

print(answer)