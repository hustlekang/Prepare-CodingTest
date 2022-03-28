# pypy3
def dfs(node,visit,graph,l,r,union):
    visit[node[0]][node[1]]=True
    union.append(node)
    population = graph[node[0]][node[1]]
    for dx,dy in zip(directionX,directionY):
        nx = node[0] + dx
        ny = node[1] + dy
        if 0<=nx<n and 0<=ny<n and l <= abs(population-graph[nx][ny]) <=r and visit[nx][ny]==False:
            dfs((nx,ny),visit,graph,l,r,union)

n,l,r=map(int,input().split())
day=0
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

directionX=[1,-1,0,0]
directionY=[0,0,-1,1]

while True:
    visit=[[False]*n for _ in range(n)]
    unions=[]
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                union = []
                dfs((i,j),visit,graph,l,r,union)
                if len(union)>1:
                    unions.append(union)

    if len(unions)==0:
        break

    for union in unions:
        totalP = 0
        for country in union:
            totalP+=graph[country[0]][country[1]]

        for country in union:
            graph[country[0]][country[1]]=totalP//len(union)

    day+=1

print(day)

############################ BFS ##########################
from collections import deque

n,l,r=map(int,input().split())
day=0
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

directionX=[1,-1,0,0]
directionY=[0,0,-1,1]

while True:
    visit=[[False]*n for _ in range(n)]
    unions=[]
    for i in range(n):
        for j in range(n):
            union = []
            if visit[i][j]==False:
                queue=deque([(i,j)])
                visit[i][j]=True
                while queue:
                    node=queue.popleft()
                    union.append(node)
                    population = graph[node[0]][node[1]]
                    for dx, dy in zip(directionX, directionY):
                        nx = node[0] + dx
                        ny = node[1] + dy
                        if 0 <= nx < n and 0 <= ny < n and l <= abs(population - graph[nx][ny]) <= r and visit[nx][
                            ny] == False:
                            queue.append((nx,ny))
                            visit[nx][ny]=True

            if len(union)>1:
                unions.append(union)

    if len(unions)==0:
        break

    for union in unions:
        totalP = 0
        for country in union:
            totalP+=graph[country[0]][country[1]]

        for country in union:
            graph[country[0]][country[1]]=totalP//len(union)

    day+=1

print(day)