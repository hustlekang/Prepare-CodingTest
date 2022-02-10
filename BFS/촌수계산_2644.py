from collections import deque
node=int(input())
start,end=map(int,input().split())
n = int(input())
answer=-1
graph=[[]for _ in range(node+1)]
visit=[False]*(node+1)

for i in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue=deque([[start,0]])
visit[start]=True
while(queue):
    v,distance=queue.popleft()
    if v==end:
        answer=distance
        break
    for nextNode in graph[v]:
        if visit[nextNode]==False:
            queue.append([nextNode,distance+1])
            visit[nextNode]=True

print(answer)
