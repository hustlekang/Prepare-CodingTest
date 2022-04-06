from collections import deque

def solution(n, vertex):
    list=[]
    cnt=0
    maxDistance=0
    visit=[False]*(n+1)
    graph=[[]for _ in range(n+1)]
    for connection in vertex:
        a,b=connection
        graph[a].append(b)
        graph[b].append(a)

    visit[1]=True
    queue=deque([(1,0)])

    while queue:
        node,distance=queue.popleft()
        before_l=len(queue)
        for nextNode in graph[node]:
            if not visit[nextNode]:
                visit[nextNode]=True
                queue.append((nextNode,distance+1))

        if before_l == len(queue):
            if distance>=maxDistance:
                maxDistance=distance
                list.append((node,distance))

    for each in list:
        if each[1]==maxDistance:
            cnt+=1

    return cnt