from collections import deque
import sys
INF = 1000000
trial=1

while True:
    N=int(sys.stdin.readline())
    if N==0:
        break

    visit=[[INF]*N for _ in range(N)]
    graph=[]
    for _ in range(N):
        graph.append(list(map(int,sys.stdin.readline().split())))

    queue= deque([(0,0)]) # x,y (cost는 큐에 넣지 않고 visit[x][y]로 구해준다, cost까지 넣어주니 시간초과)
    visit[0][0]=graph[0][0]

    while queue:
        x,y=queue.popleft()
        for dx,dy in zip([0,0,-1,1],[1,-1,0,0]):
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N and  graph[nx][ny]+visit[x][y] < visit[nx][ny]:
                visit[nx][ny]=graph[nx][ny]+visit[x][y]
                queue.append((nx,ny))

    print("Problem {}: {}".format(trial,visit[N-1][N-1]))
    trial+=1