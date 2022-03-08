# 간선의 비용이 다 다르기 때문에 돌아서 가는 길이 거리가 더 짧을 수도 있다 => visit으로 판별하는 것이 아니고 거리 값으로 판별
from collections import deque
def solution(N, road, K):
    graph=[[]for _ in range(N+1)]
    graphDistance = [1000000]*(N+1)
    answer=0

    for line in road:
        nodeA,nodeB,distance=line[0],line[1],line[2]
        graph[nodeA].append((nodeB,distance))
        graph[nodeB].append((nodeA, distance))
    #노드 사이 길이 2개 이상일 시, 거리가 작은 길이 앞에 오게끔 정렬을 해서 먼저 넣어준다.
    for connection in graph:
        connection.sort(key=lambda x:x[1])

    queue=deque([(1,0)])
    while(queue):
        node,distance=queue.popleft()
        if distance<=K:
            graphDistance[node]=distance
        #간선이 2개 이상이어도 distance가 짧은것부터 정렬 되어 있어서 차례대로 for문 돌려도 OK
        for nextNodeInfo in graph[node]:
            if distance+nextNodeInfo[1]<graphDistance[nextNodeInfo[0]]:
                graphDistance[nextNodeInfo[0]]=distance+nextNodeInfo[1]
                queue.append((nextNodeInfo[0],distance+nextNodeInfo[1]))

    for distance in graphDistance:
        if distance<=K:
            answer+=1

    return answer