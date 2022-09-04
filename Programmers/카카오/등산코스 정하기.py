import heapq

def solution(n, paths, gates, summits):
    INF = 10**8
    summits = set(summits)
    answer = [-1, INF]
    connections = [[] for _ in range(n+1)]
    intensity = [INF] * (n+1)
    minHeap = [(0,gate) for gate in gates]

    for path in paths:
        a,b,d = path
        connections[a].append((b, d))
        connections[b].append((a, d))

    while minHeap:
        distance, node = heapq.heappop(minHeap)
        if distance < intensity[node]:
            intensity[node] = distance
            if node in summits: # set이기 때문에 O(1)
                continue

            for connection in connections[node]:
                nextNode, nextDistance = connection
                newIntensity = max(nextDistance, distance)
                if newIntensity < intensity[nextNode]:
                    heapq.heappush(minHeap, (newIntensity, nextNode))

    for summit in summits:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
        elif intensity[summit] == answer[1] and summit < answer[0]:
            answer[0] = summit

    return answer

# test4 틀리고 test15~17 시간초과
# from collections import deque
#
# def solution(n, paths, gates, summits):
#     answer = [None ,10**7]
#     connections = [[] for _ in range(n+1)]
#     nodeType = [0] * (n+1) # 0: 일반노드, 1 : 게이트 , 2 : 봉우리
#
#     for path in paths:
#         a,b,d = path
#         connections[a].append((b,d))
#         connections[b].append((a,d))
#     for gate in gates:
#         nodeType[gate] = 1
#     for summit in summits:
#         nodeType[summit] = 2
#
#     # 모든 게이트에서 조사
#     for gate in gates:
#         queue = deque([(gate,0)]) # 노드,최대 간선
#         visit = [10**7] * (n+1)
#         visit[gate] = 0
#
#         while queue:
#             node, intensity = queue.popleft()
#             if nodeType[node] == 2:
#                 if intensity < answer[1]:
#                     answer = [node, intensity]
#                 elif intensity == answer[1]:
#                     answer = [min(answer[0],node), intensity]
#                 continue
#
#             for connection in connections[node]:
#                 next, d = connection
#                 newIntensity = max(intensity,d)
#                 if newIntensity < visit[next] and nodeType[next] != 1 and newIntensity <= answer[1]:
#                     visit[next] = newIntensity
#                     queue.append((next, newIntensity))
#
#     return answer