#BFS
from collections import deque
m=int(input())
graph=[]
answer=[[0]*m for _ in range(m)]

for _ in range(m):
    graph.append(list(map(int,input().split())))

for node in range(m):
    visit=[False]*m
    queue=deque([node])
    while(queue):
        v=queue.popleft()
        for idx in range(m):
            if graph[v][idx]==1 and visit[idx]==False:
                queue.append(idx)
                visit[idx]=True
                answer[node][idx]=1

for line in answer:
    for each in line:
        print(each,end=" ")
    print()