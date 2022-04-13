# 테스트케이스 5개 시간초과 나는데 모르겠당
from collections import deque
from copy import deepcopy
from itertools import combinations

def solution(n, weak, dist):
    dist.sort()
    distances = [] # weak[]에서 오른쪽 노드와의 거리
    answer = -1

    for i in range(len(weak) - 1):
        distances.append(weak[i + 1] - weak[i])

    distances.append(n - weak[-1] + weak[0])

    distanceBetweenNode = [] # (i번노드와,j번노드,사이의거리)
    for i in range(len(weak) - 1):
        distanceBetweenNode.append((i, i + 1, distances[i]))
    distanceBetweenNode.append((len(weak) - 1, 0, distances[-1]))
    distanceBetweenNode.sort(key=lambda x: x[2])

    connection = {} # connection[현재노드][연결된노드]= 의 거리
    nowConnected = [[] for _ in range(len(weak))] # 현재 노드에 연결된 노드들 2차원 리스트
    for i in range(len(weak)):
        nowConnected[i].append((i + 1) % len(weak))
        nowConnected[i].append((i - 1) % len(weak))
        connection[i] = {
            (i + 1) % len(weak): distances[i],
            (i - 1) % len(weak): distances[(i - 1) % len(weak)]
        }

    cut = 1
    while True:
        combination=combinations(distanceBetweenNode,cut)
        noMore=False
        for willbeCut in combination: #어떤 얘들 연결을 끊고 갈껀지
            isPossible = True
            nowConnected2 = deepcopy(nowConnected)  # 짜를 때마다 연결된 요소를 새롭게 초기화 해줘야함
            canGoArr = deepcopy(dist)

            for each in willbeCut:
                nowConnected2[each[0]].remove(each[1]) #연결 제거
                nowConnected2[each[1]].remove(each[0]) #연결 제거

            visit = [False] * len(weak)
            parts = []
            for node in range(len(weak)):  # 모든 노드에 대하여
                queue = deque([])
                length = 0
                if not visit[node]:  # 탐색 안했더라면 연결된 요소를 구한다
                    visit[node] = True
                    queue.append(node)
                    while queue:
                        v = queue.popleft()
                        for nextNode in nowConnected2[v]:
                            if not visit[nextNode]:
                                visit[nextNode] = True
                                length += connection[v][nextNode]
                                queue.append(nextNode)

                    parts.append(length)

            parts.sort()  # 연결 요소들 사이의 거리들을 짧은 순부터 점검 가능한 사람이 있나 확인
            while parts:
                isdel = False
                for canGo in canGoArr:
                    if canGo >= parts[0]:
                        parts.pop(0)
                        canGoArr.remove(canGo)
                        isdel = True
                        break

                if not isdel:  # 연결 길이 만큼 이동할 수 있는 사람이 없으니
                    isPossible = False  # 불가능
                    break

            if isPossible:
                answer = cut
                noMore=True
                break
        if noMore:
            break
        cut += 1

    return answer



# 노드 사이 거리가 가장 긴 순으로 잘라야 한다고 생각했었음
# 아닌 상황도 있어서 조합으로 해야할듯

    # while distanceBetweenNode: # 이어진 부분중 긴 부분부터 짤라서 가능한지 확인
    #     isPossible = True
    #     canGoArr = deepcopy(dist)
    #     node1, node2, d = distanceBetweenNode.pop()
    #     nowConnected[node1].remove(node2) # 연결 제거
    #     nowConnected[node2].remove(node1) # 연결 제거
    #     visit = [False] * len(weak)
    #     parts = []
    #     for node in range(len(weak)):  # 모든 노드에 대하여
    #         queue = deque([])
    #         length = 0
    #         if not visit[node]:  # 탐색 안했더라면 연결된 요소를 구한다
    #             visit[node] = True
    #             queue.append(node)
    #             while queue:
    #                 v = queue.popleft()
    #                 for nextNode in nowConnected[v]:
    #                     if not visit[nextNode]:
    #                         visit[nextNode] = True
    #                         length += connection[v][nextNode]
    #                         queue.append(nextNode)
    #
    #             parts.append(length)
    #
    #     parts.sort() # 연결 요소들 사이의 거리들을 짧은 순부터 점검 가능한 사람이 있나 확인
    #     while parts:
    #         isdel = False
    #         for canGo in canGoArr:
    #             if canGo >= parts[0]:
    #                 parts.pop(0)
    #                 canGoArr.remove(canGo)
    #                 isdel = True
    #                 break
    #
    #         if not isdel: # 연결 길이 만큼 이동할 수 있는 사람이 없으니
    #             isPossible = False # 불가능
    #             break
    #
    #     if isPossible:
    #         answer = cut
    #         break
    #
    #     cut += 1