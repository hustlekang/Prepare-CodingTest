import sys, heapq

input = sys.stdin.readline
INF = 10 ** 8

# 시작점에서 모든 노드들 사이의 최단거리를 담은 배열을 반환
def dijkstra(start, n):
    global connection
    distance = [INF] * (n + 1)
    minHeap = [(0, start)]
    distance[start] = 0

    while minHeap:
        dis, node = heapq.heappop(minHeap)
        if dis > distance[node]: continue

        for nextDis, nextNode in connection[node]:
            newDis = dis + nextDis
            if newDis < distance[nextNode]:
                distance[nextNode] = newDis
                heapq.heappush(minHeap, (newDis, nextNode))

    return distance

# 간선의 비용을 다 짝수로 만들고 지나야 하는 간선은 홀수로 만들면
# 짝수 + 짝수 = 짝수이므로
# 만약 지나야 하는 간선을 포함하게 되면 무조건 거리가 홀수가 나옴
if __name__ == '__main__':
    trial = int(input())

    for _ in range(trial):
        # 노드개수, 링크개수, 목적지 후보 개수
        n, m, t = map(int, input().split(' '))

        connection = [[] for _ in range(n+1)]
        targets = set()

        # s: 출발지, 최단거리에 g-h가 포함되어있다
        s, g, h = map(int, input().split(' '))
        smellLoad = {(g,h),(h,g)}

        for _ in range(m):
            # a와 b 연결 거리 d
            a, b, d = map(int, input().split(' '))

            if (a,b) in smellLoad: # 지나야 하는 링크는 2곱하고 1 빼서 홀수로 만듬
                connection[a].append((int(d*2) -1, b))
                connection[b].append((int(d*2) - 1, a))
            # 나머지 링크들은 2곱해서 짝수로 만듬
            connection[a].append((int(d * 2), b))
            connection[b].append((int(d * 2), a))

        for _ in range(t):
            nodeNum = int(input())
            targets.add(nodeNum)

        distance = dijkstra(s, n)

        possibleTargets = []
        for target in targets:
            if distance[target] % 2 == 1: # 최단거리가 홀수면 지나야 하는 링크 지난거임
                possibleTargets.append(target)

        answer = " ".join(map(str, sorted(possibleTargets)))
        print(answer)


## BFS 로는 에바
import sys
from collections import deque

input = sys.stdin.readline
INF = 10 ** 8

if __name__ == '__main__':
    trial = int(input())

    for _ in range(trial):
        # 노드개수, 링크개수, 목적지 후보 개수
        n, m, t = map(int, input().split(' '))

        connection = [[] for _ in range(n+1)]
        target = set()
        targetInfo = {}

        # s: 출발지, 최단거리에 g-h가 포함되어있다
        s, g, h = map(int, input().split(' '))
        smellLoad = {(g,h),(h,g)}
        for _ in range(m):
            # a와 b 연결 거리 d
            a, b, d = map(int, input().split(' '))
            connection[a].append((d, b))
            connection[b].append((d, a))

        for _ in range(t):
            nodeNum = int(input())
            target.add(nodeNum)
            targetInfo[nodeNum] = [False, INF]

        visit = [INF] * (n+1)
        visit[s] = 0
        queue = deque([(s, 0, False)]) #노드번호, 거리, g-h 지났는지

        while queue:
            node, d, isPassed = queue.popleft()

            if node in target: # 목적지에 도달 했으면
                if d < targetInfo[node][1]: # 현재 경로가 더 짧을 때 갱신
                    targetInfo[node] = [isPassed, d]

                # !!!
                elif d == targetInfo[node][1]: # 경로 길이가 같으면
                    if not targetInfo[node][0] and isPassed:
                        targetInfo[node][0] = True
                # !!!continue하면 안되고 계쏙 탐색해야댐, target 다음 target 일 수 있음
                # continue ㄴㄴ
                # 하지만 이러면 시간초과

            for distance, nextNode in connection[node]:
                newDis = d + distance
                if newDis <= visit[nextNode]: # 거리가 더 작을 때만 ㄱㄱ
                    newIsPassed = isPassed
                    if not isPassed and (node,nextNode) in smellLoad:
                        newIsPassed = True
                    visit[nextNode] = newDis
                    queue.append((nextNode, newDis, newIsPassed))

        possibleTarget = []
        for target in targetInfo.keys():
            if targetInfo[target][0] and targetInfo[target][1] != INF: # g-h 지나온 경우만
                possibleTarget.append(target)

        answer = " ".join(map(str,sorted(possibleTarget)))
        print(answer)