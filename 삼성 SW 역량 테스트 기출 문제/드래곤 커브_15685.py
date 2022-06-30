def dragoncurve(x,y,d,g):
    direction = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}
    if g==0:
        dx,dy=direction[d]
        nx=x+dx
        ny=y+dy
        return [(x,y),(nx,ny)]

    points=dragoncurve(x,y,d,g-1)
    lastPoint=points[-1]
    for point in reversed(dragoncurve(x,y,d,g-1)): #회전하면 첫번째 점이 끝점이 되기 때문에  lastPoint 유지를 위해 reverse한 다음 회전함
        points.append((-point[1]+lastPoint[1]+lastPoint[0],point[0]-lastPoint[0]+lastPoint[1])) # 끝점 기준 90도 회전
    return points

N=int(input())
cnt=0
graph=[[0]*101 for _ in range(101)]
for _ in range(N):
    x,y,d,g=map(int,input().split())
    for point in dragoncurve(x,y,d,g):
        graph[point[1]][point[0]]=1

for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i+1][j]==1 and graph[i][j+1] ==1 and graph[i+1][j+1]==1:
            cnt+=1

print(cnt)