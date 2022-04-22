# 시작 노드에서 다른 노드들까지 거리를 초기화, 시작노드 방문처리
# 가장 가까운 방문하지 않은 노드를 거쳐서 가는 방식이 원래 거리보다 짧으면 갱신
# PyPy3
INF=10000000
V,E=map(int,input().split())
K=int(input())
visit=[False]*(V+1)
distances=[INF]*(V+1) # 인덱스 노드 까지의 거리
graph=[{} for _ in range(V+1)] #graph[k] 는 k번 노드와 연결된 노드들의 번호와 거리
for _ in range(E):
    a,b,d=map(int,input().split())
    if b in graph[a].keys():
        if d<graph[a][b]:
            graph[a][b] = d
    else:
        graph[a][b]=d

def shortestNode(distance,visit):
    idx = -1
    minimum = INF
    for i in range(len(distance)):
        if distance[i] < minimum and visit[i]==False:
            idx = i
            minimum = distance[i]

    return idx

visit[K]=True
for nextNode in graph[K].keys():
    distances[nextNode]=graph[K][nextNode]

while True:
    shortest_idx=shortestNode(distances,visit)
    if shortest_idx==-1:
        break

    visit[shortest_idx]=True
    untilShortestNode=distances[shortest_idx]
    for nextNode in graph[shortest_idx].keys():
        if untilShortestNode+graph[shortest_idx][nextNode]<distances[nextNode]: # 거쳐서 가는게 기존길보다 빠르면
            distances[nextNode]=untilShortestNode + graph[shortest_idx][nextNode]

for i in range(1,V+1):
    if i==K:
        print(0)
    elif distances[i]==INF:
        print('INF')
    else:
        print(distances[i])

##############################
import heapq

INF=10000000
V,E=map(int,input().split())
K=int(input())
visit=[False]*(V+1)
distances=[INF]*(V+1) # 인덱스 노드 까지의 거리
graph=[{} for _ in range(V+1)] #graph[k] 는 k번 노드와 연결된 노드들의 번호와 거리
heap=[] # 가장 가까운 노드 찾기위한 최소힙
for _ in range(E):
    a,b,d=map(int,input().split())
    if b in graph[a].keys():
        if d<graph[a][b]:
            graph[a][b] = d
    else:
        graph[a][b]=d

visit[K]=True # 초기 노드끼리 거리 세팅
for nextNode in graph[K].keys():
    heapq.heappush(heap,(graph[K][nextNode],nextNode))
    distances[nextNode]=graph[K][nextNode]

while heap:
    untilShortestNode,shortest_idx=heapq.heappop(heap)
    if visit[shortest_idx]:
        continue

    visit[shortest_idx]=True

    for nextNode in graph[shortest_idx].keys():
        if untilShortestNode+graph[shortest_idx][nextNode]<distances[nextNode]: # 거쳐서 가는게 기존길보다 빠르면
            new_distance=untilShortestNode + graph[shortest_idx][nextNode]
            distances[nextNode]=untilShortestNode + graph[shortest_idx][nextNode] # 거리 업데이트
            heapq.heappush(heap,(new_distance,nextNode)) # 힙에 갱신된 정보 삽입

for i in range(1,V+1):
    if i==K:
        print(0)
    elif distances[i]==INF:
        print('INF')
    else:
        print(distances[i])