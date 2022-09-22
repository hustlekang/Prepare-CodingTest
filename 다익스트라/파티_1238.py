from collections import defaultdict
import heapq

def dijkstra(start, end):
    global connection
    minHeap = []
    distanceArr = [INF] * (N + 1)
    distanceArr[start] = 0
    heapq.heappush(minHeap, (0, start))

    while minHeap:
        distance, node = heapq.heappop(minHeap)
        if distanceArr[node] < distance:
            continue

        for nextNode, dis in connection[node]:
            newDis = distance + dis
            if distanceArr[nextNode] > newDis:
                distanceArr[nextNode] = newDis
                heapq.heappush(minHeap,(newDis, nextNode))

    return distanceArr[end]

if __name__ == '__main__':
    INF = 10 ** 8
    maxDis = 0
    N, M, X = map(int, input().split(' '))
    connection = defaultdict(list)
    for _ in range(M):
        start, end, cost = map(int, input().split(' '))
        connection[start].append((end, cost))

    for node in range(1,N+1):
        go = dijkstra(node, X)
        back = dijkstra(X, node)
        totalDis = go + back
        maxDis = max(maxDis, totalDis)

    print(maxDis)