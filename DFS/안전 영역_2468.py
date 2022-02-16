from collections import deque
import sys
m=int(input())
graph=[]
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]
answer=[]
for _ in range(m):
    graph.append(list(map(int,sys.stdin.readline().split())))

for height in range(100):
    visit = [[False] * m for _ in range(m)]
    cnt=0
    queue=deque([])
    for x in range(m):
        for y in range(m):
            if visit[x][y]==False and graph[x][y]>height:
                queue.append([x,y])
                visit[x][y]=True
                while (queue):
                    v = queue.popleft()
                    for dx,dy in zip(directionX,directionY):
                        nx = v[0]+dx
                        ny= v[1]+dy
                        if 0<=nx<m and 0<=ny<m and visit[nx][ny]==False and graph[nx][ny]>height:
                            queue.append([nx,ny])
                            visit[nx][ny]=True
                cnt+=1
    answer.append(cnt)

print(max(answer))