from collections import deque

def choiceBuildings(N): # 빌딩번호 조합 반환
    choice = []
    for i in range(1,N):
        for j in range(i+1,N+1):
            choice.append((i,j))
    return choice

def setConnection(N,M): # 도로 연결 상태 반환
    connection = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        connection[a].append(b)
        connection[b].append(a)
    return connection

def pickOne(array): # 중복 시 1순위 반환
    if len(array) == 1:
        return array[0]
    array.sort(key=lambda x:x[1])
    array.sort(key=lambda x:x[0])
    return array[0]

def main():
    N, M = map(int, input().split())
    connection = setConnection(N,M)
    minDis = 100000
    answerList = []

    for combi in choiceBuildings(N):
        building_1, building_2 = combi
        visit = [1000] * (N + 1)
        visit[building_1] = 0
        visit[building_2] = 0

        queue = deque([])
        queue.append((building_1, 0))
        queue.append((building_2, 0))

        while queue:
            n, distance = queue.popleft()
            for next in connection[n]:
                if distance + 1 < visit[next]:
                    visit[next] = distance + 1
                    queue.append((next, distance + 1))

        d = (sum(visit) - 1000) * 2 # visit[0]=1000 은 빌딩 번호 인덱스 맞추려는 의미없는 값이므로 -1000
        if d < minDis:
            answerList = [(building_1,building_2,d)]
            minDis = d
        elif d == minDis:
            answerList.append((building_1,building_2,d))

    answer = pickOne(answerList)
    print(answer[0], answer[1], answer[2])

main()


# 플로이드 와샬 ---------------------------------------------------------------------
INFINITY = 100000
N, M = map(int, input().split())
graph = [[INFINITY]*(N+1) for _ in range(N+1)]
answer = (None, None, None)

for a in range(N+1):
    graph[a][a] = 0

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for mid in range(1,N+1):
    for start in range(1,N+1):
        for end in range(1,N+1):
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])

minDistance = INFINITY
for chicken_1 in range(1,N+1):
    for chicken_2 in range(chicken_1+1,N+1):
        distance = 0
        for building in range(1,N+1):
            distance += min(graph[chicken_1][building] * 2, graph[chicken_2][building] * 2)

        if distance < minDistance: # 건물 번호 작은 순부터 for문 도니까 작을 때만 갱신
            answer = [chicken_1,chicken_2,distance]
            minDistance = distance

print(" ".join(map(str,answer)))