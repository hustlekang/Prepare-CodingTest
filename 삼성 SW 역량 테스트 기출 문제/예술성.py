# 코드트리
# 22년 상반기 오전 2번

from collections import deque

def rotate_4parts():
    global n, graph
    if len(graph) == 3:
        return

    k = (n-1) // 2

    part1 = [row[:k] for row in graph[:k]] # 왼쪽위
    part2 = [row[-k:] for row in graph[:k]] # 오른쪽위
    part3 = [row[:k] for row in graph[-k:]] # 왼쪽아래
    part4 = [row[-k:] for row in graph[-k:]] # 오른쪽아래

    newPart1 = rotate(part1)
    newPart2 = rotate(part2)
    newPart3 = rotate(part3)
    newPart4 = rotate(part4)

    # graph에 회전된것 반영
    for i in range(k):
        for j in range(k):
            graph[i][j] = newPart1[i][j] # 왼쪽 위 업데이트
            graph[i][j+k+1] = newPart2[i][j] # 오른쪽 위
            graph[i+k+1][j] = newPart3[i][j] # 왼쪽 아래
            graph[i+k+1][j+k+1] = newPart4[i][j] # 오른쪽 아래


def rotate_crossBar():
    global graph, n
    col = [row[n//2] for row in graph] # 가운데 세로
    row = graph[n//2][::-1] # 가운데 가로 리버스

    graph[n//2] = col
    for i in range(n):
        graph[i][n//2] = row[i]


def rotate(arr_2d):
    m = len(arr_2d)
    rotated = [[0]*m for _ in range(m)]

    for i in range(m):
        for j in range(m):
            rotated[j][m-1-i] = arr_2d[i][j]

    return rotated

# 그룹 찾는 함수
def findGroup():
    global n, graph
    visit = [[False] * n for _ in range(n)]
    id = 0
    groups = {} # {0 :[숫자,{(x1,y1),...}] }
    queue = deque([])

    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                queue.append((i,j,graph[i][j]))
                visit[i][j] = True
                groups[id] = [graph[i][j], {(i, j)}]

                while queue:
                    x, y, number = queue.popleft()
                    for dx, dy in zip([1,-1,0,0], [0,0,-1,1]):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == number and not visit[nx][ny]:
                            visit[nx][ny] = True
                            groups[id][1].add((nx,ny))
                            queue.append((nx, ny, number))
                id += 1

    return groups


def getArtScore():
    score = 0
    group = findGroup() # {0 :[숫자,{(x1,y1),...}] }
    n = len(group.keys()) # 그룹이 4개면 인덱스는 0 1 2 3

    for i in range(n):
        for j in range(i+1, n):
            numberGroup1, cntGroup1 = group[i][0], len(group[i][1])
            numberGroup2, cntGroup2 = group[j][0], len(group[j][1])
            adjacentCnt = 0

            for x,y in group[i][1]:
                for dx, dy in zip([0,0,-1,1], [1,-1,0,0]):
                    nx, ny = x + dx, y + dy
                    if (nx,ny) in group[j][1]:
                        adjacentCnt += 1

            score += int((cntGroup1 + cntGroup2) * numberGroup1 * numberGroup2 * adjacentCnt)

    return score


if __name__ == '__main__':
    n = int(input())
    graph = [list(map(int, input().strip().split())) for _ in range(n)]

    score = getArtScore()

    for _ in range(3):
        rotate_4parts()
        rotate_crossBar()
        score += getArtScore()

    print(score)