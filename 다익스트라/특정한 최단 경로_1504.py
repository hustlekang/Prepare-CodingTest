import sys,heapq
from collections import defaultdict

def shortestPath(start,target,visit,distance,connection):
    minHeap = []
    visit[start] = True
    distance[start] = 0
    for next in connection[start]:
        dis, node = next
        distance[node] = dis
        heapq.heappush(minHeap, next)

    while minHeap:
        dis, node = heapq.heappop(minHeap)
        if not visit[node]:
            visit[node] = True
            for next in connection[node]:
                new_dis, new_node = next
                if dis + new_dis < distance[new_node]:
                    distance[new_node] = dis + new_dis
                    heapq.heappush(minHeap, (dis+new_dis,new_node))

    return distance[target]

N,E=map(int,sys.stdin.readline().split())
connection = defaultdict(list)
answer=sys.maxsize

for _ in range(E):
    node1,node2,distance=map(int,sys.stdin.readline().split())
    connection[node1].append((distance,node2))
    connection[node2].append((distance,node1))

midPoint1,midPoint2=map(int,sys.stdin.readline().split())

distance_1_midPoint1=shortestPath(1,midPoint1,[False]*(N+1),[sys.maxsize]*(N+1),connection)
distance_midPoint1_midPoint2=shortestPath(midPoint1,midPoint2,[False]*(N+1),[sys.maxsize]*(N+1),connection)
distance_midPoint2_N=shortestPath(midPoint2,N,[False]*(N+1),[sys.maxsize]*(N+1),connection)

distance_1_midPoint2=shortestPath(1,midPoint2,[False]*(N+1),[sys.maxsize]*(N+1),connection)
distance_midPoint2_midPoint1=shortestPath(midPoint2,midPoint1,[False]*(N+1),[sys.maxsize]*(N+1),connection)
distance_midPoint1_N=shortestPath(midPoint1,N,[False]*(N+1),[sys.maxsize]*(N+1),connection)

# 1 -> midPoint1 -> midPoint2 -> N
if sys.maxsize not in [distance_1_midPoint1,distance_midPoint1_midPoint2,distance_midPoint2_N]:
    answer=distance_1_midPoint1+distance_midPoint1_midPoint2+distance_midPoint2_N
# 1 -> midPoint2 -> midPoint1 -> N
if sys.maxsize not in [distance_1_midPoint2,distance_midPoint2_midPoint1,distance_midPoint1_N]:
    answer = min(answer,distance_1_midPoint2+distance_midPoint2_midPoint1+distance_midPoint1_N)

if answer==sys.maxsize:
    answer=-1

print(answer)