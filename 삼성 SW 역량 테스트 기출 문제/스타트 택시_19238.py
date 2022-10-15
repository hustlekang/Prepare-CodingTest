from collections import deque

# 가장 가까운 거리의 승객 정보를 반환 (x, y, distance)
def findPassenger(taxiPoint): # (x,y)
    global N, startPoint, graph
    visit = [[False] * N for _ in range(N)]
    visit[taxiPoint[0]][taxiPoint[1]] = True
    closest = (-1,-1,-1)
    minDis = 1000
    queue = deque([(taxiPoint[0], taxiPoint[1], 0)])

    while queue:
        x, y, distance = queue.popleft()
        if (x, y) in startPoint:
            if distance < minDis:
                minDis = distance
                closest = (x,y,distance)
            elif distance == minDis:
                if x < closest[0]:
                    closest = (x, y, distance)
                elif x == closest[0] and y < closest[1]:
                    closest = (x, y, distance)

        for dx, dy in zip([0,0,1,-1], [1,-1,0,0]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0 and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return closest

def caculateDistance(startPoint):
    global N, endPoint, graph
    visit = [[False] * N for _ in range(N)]
    visit[startPoint[0]][startPoint[1]] = True
    queue = deque([(startPoint[0], startPoint[1], 0)])

    while queue:
        x, y, distance = queue.popleft()
        if (x,y) == endPoint[startPoint]:
            return distance

        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0 and not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny, distance + 1))

    return -1

if __name__ == '__main__':
    N, M, fuel = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    a, b = map(lambda x : int(x) - 1, input().split())
    taxiPoint = (a, b)
    startPoint = set()
    endPoint = {}
    for _ in range(M):
        a, b, c, d = map(lambda x : int(x) - 1, input().split())
        startPoint.add((a,b))
        endPoint[(a,b)] = (c,d)

    for _ in range(M):
        x1, y1, d1 = findPassenger(taxiPoint)
        if x1 == -1 and y1 == -1: # 가장 가까운 손님을 못찾는다 ? 벽으로 막혀서 못가는 상황
            fuel = -1
            break

        d2 = caculateDistance((x1,y1))
        if d2 < 0: # 거리가 -1 이다? 벽으로 막혀서 못가는 상황
            fuel = -1
            break

        if fuel - (d1 + d2) < 0:
            fuel = -1
            break

        fuel = fuel - (d1 + d2) + int(2 * d2) # 연료 갱신
        startPoint.remove((x1,y1)) # 승객 갱신
        taxiPoint = (endPoint[(x1,y1)]) # 택시 위치 갱신

    print(fuel)