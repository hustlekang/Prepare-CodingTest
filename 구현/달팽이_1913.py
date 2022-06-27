N=int(input())
K=int(input())

graph=[[0]*N for _ in range(N)]
differ=[(1,0),(0,1),(-1,0),(0,-1)]
x,y=0,0
differ_idx=0
number=int(N**2)
while number>0:
    graph[x][y]=number
    dx, dy = differ[differ_idx%4]
    nx = x+ dx
    ny= y + dy
    if 0<=nx<N and 0<=ny<N and graph[nx][ny]==0:
        x = nx
        y = ny
    else:
        differ_idx+=1
        dx, dy = differ[differ_idx % 4]
        nx = x + dx
        ny = y + dy
        x=nx
        y=ny

    number-=1

for line in graph:
    print(" ".join(map(str,line)))
for i in range(N):
    for j in range(N):
        if graph[i][j]==K:
            print(i+1,j+1)
            break