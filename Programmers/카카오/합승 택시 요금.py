# 플로이드 와샬 알고리즘 O(n^3)
from sys import maxsize
def solution(n, s, a, b, fares):
    graph=[[maxsize]*(n+1) for _ in range(n+1)] # 노드와 노드사이 거리를 무한대로 초기화
    for i in range(1,n+1): # 자기 자신으로 가는 거리는 0
        graph[i][i]=0

    for fare in fares: # 입력으로 주어진 상태로 그래프 초기화
        nodeA, nodeB, d = fare
        graph[nodeA][nodeB] = d
        graph[nodeB][nodeA] = d
    # D(a,b) = min( D(a,b), D(a,k)+D(k,b))
    for k in range(1,n+1): # 모든 노드에 대하여 k를 거쳐가는게 더 빠르면 갱신
        for start in range(1,n+1):
            for end in range(1,n+1):
                graph[start][end]=min(graph[start][end],graph[start][k]+graph[k][end])

    answer = graph[s][a]+graph[s][b] # 각자 타고 가는 요금
    for k in range(1,n+1): # k:같이타다 각자 가는 지점 , 요금 = D(s,k) + D(k,a) + D(k,b)
        answer= min(answer,graph[s][k]+graph[k][a]+graph[k][b])

    return answer

# s~a 까지 경로, s~b까지 모든 경로를 구해서 겹치는 경로에 해당하는 금액 빼주고 계산하는 식
#
from copy import deepcopy
from collections import deque

def solution(n, s, a, b, fares):
    a_ways = []
    b_ways = []
    connection = [[] for _ in range(n + 1)]
    for fare in fares:
        nodeA, nodeB, d = fare
        connection[nodeA].append([nodeB, d])
        connection[nodeB].append([nodeA, d])
    a_connected = [connected[0] for connected in connection[a]]
    b_connected = [connected[0] for connected in connection[b]]
    visit_init = [False] * (n + 1)
    visit_init[s] = True
    queue = deque([(s, 0, [], visit_init)])
    while queue:
        node, d, way, visit = queue.popleft()

        if node == a:
            a_ways.append((d, way))
            if not b in a_connected:
                continue

        elif node == b:
            b_ways.append((d, way))
            if not a in b_connected:  # 테스트3 처럼 b에 도달해도 b에서 a로 가는 길이 있으면 계속 탐색 해야함
                continue

        for next in connection[node]:
            nextNode, distance = next
            if visit[nextNode] == False:
                copyVisit = deepcopy(visit)
                copyWay = deepcopy(way)
                copyVisit[nextNode] = True
                copyWay.append((nextNode, distance))
                queue.append((nextNode, d + distance, copyWay, copyVisit))

    a_ways.sort(key=lambda x: x[0])
    b_ways.sort(key=lambda x: x[0])
    answer = a_ways[0][0] + b_ways[0][0]

    for a_info in a_ways:
        a_total, a_way = a_info
        for b_info in b_ways:
            b_total, b_way = b_info
            saveMoney = 0
            for a_each, b_each in zip(a_way,
                                      b_way):  # [(1, 10), (3, 41), (5, 24), (6, 2)] / [(1, 10), (3, 41), (2, 22)]
                if a_each[0] == b_each[0]:
                    saveMoney += a_each[1]
                else:
                    break
            if saveMoney != 0:  # 겹치는 길이 있는 부분
                if a_total + b_total - saveMoney < answer:
                    answer = a_total + b_total - saveMoney

    return answer

