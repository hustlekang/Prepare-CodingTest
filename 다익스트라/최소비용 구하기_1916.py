import sys
import heapq
from collections import defaultdict

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
bus=defaultdict(list) # 출발지 : [(비용1,도착지1),(비용2,도착지2)...]
minHeap=[]

for _ in range(M):
    start,arrive,cost=map(int,sys.stdin.readline().split())
    bus[start].append((cost,arrive))

startNode,destinationNode=map(int,sys.stdin.readline().split())

distance=[sys.maxsize]*(N+1)
visit=[False]*(N+1)
distance[startNode]=0
visit[startNode]=True
for next in bus[startNode]:
    cost,node=next
    distance[node]=min(cost,distance[node]) # 경로가 여러개면 가장 짧은 거리로 가야지
    heapq.heappush(minHeap,next)

while minHeap:
    cost,node=heapq.heappop(minHeap)
    if not visit[node]:
        visit[node]=True
        for next in bus[node]: # next = 징검다리와 이어진 노드들
            new_cost,new_node=next
            if new_cost+cost < distance[new_node]:
                distance[new_node]=new_cost+cost
                heapq.heappush(minHeap,(new_cost+cost,new_node))

print(distance[destinationNode])