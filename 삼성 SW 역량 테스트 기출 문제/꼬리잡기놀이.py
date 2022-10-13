# 코드트리
# 22년 상반기 오후 1번

from collections import  deque

def init():
    global graph, n, groups
    visit = [[False] * n for _ in range(n)]
    queue = deque([])

    for i in range(n):
        for j in range(n):
            people = 0
            if not visit[i][j] and graph[i][j] != 0:
                if graph[i][j] != 4:
                    people += 1
                sequence = deque([])
                coordinate = []
                sequence.append(graph[i][j])
                coordinate.append((i, j))
                queue.append((i, j, graph[i][j]))
                visit[i][j] = True

                while queue:
                    x, y, num = queue.popleft()
                    for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny] and graph[nx][ny] != 0:
                            sequence.append(graph[nx][ny])
                            coordinate.append((nx, ny))
                            queue.append((nx, ny, graph[nx][ny]))
                            visit[nx][ny] = True
                            if graph[nx][ny] != 4:
                                people += 1
                            break

                groups.append({
                    'length' : len(sequence),
                    'people' : people,
                    'headIdx': sequence.index(1),
                    'tailIdx': sequence.index(3),
                    'sequence' : sequence,
                    'coordinate' : coordinate,
                    'coordinateSet' : set(coordinate)
                })


def move():
    global groups, ballInfo, n
    for group in groups:
        rightIdx = (group['tailIdx'] + 1) % group['length'] # 헤더 오른쪽의 인덱스
        if group['sequence'][rightIdx] == 2  : # 오른쪽으로
            group['sequence'].rotate()
            group['headIdx'] = (group['headIdx'] + 1) % group['length']
            group['tailIdx'] = (group['tailIdx'] + 1) % group['length']

        else:
            group['sequence'].rotate(-1)
            group['headIdx'] = (group['headIdx'] + (group['length'] - 1)) % group['length']
            group['tailIdx'] = (group['tailIdx'] + (group['length'] - 1)) % group['length']

    for i in range(n):
        ballInfo[i+1] = (i,0,0,1)

    for i in range(n):
        ballInfo[i+1+n] = (n-1,i,-1,0)

    for i in range(n):
        ballInfo[i+1+int(2*n)] = (n-1-i,n-1,0,-1)

    for i in range(n):
        ballInfo[i+1+int(3*n)] = (0,n-1-i,1,0)


def getScore(trial):
    global n, groups, ballInfo # n트 : (시작x,시작y,dx,dy)
    if trial > n*4:
        if trial % (n*4) == 0:
            trial = int(n*4)
        else:
            trial %= (n*4)
    x, y, dx, dy = ballInfo[trial]

    for _ in range(n):
        for group in groups:
            if (x,y) in group['coordinateSet']:
                idx = group['coordinate'].index((x, y))
                if group['sequence'][idx] != 4: # 사람이 맞은것
                    if group['sequence'][idx] == 3: # 꼬리사람이 맞은것
                        temp = group['sequence'][group['headIdx']] # 헤드값
                        group['sequence'][group['headIdx']] = group['sequence'][group['tailIdx']]
                        group['sequence'][group['tailIdx']] = temp
                        group['headIdx'], group['tailIdx'] = group['tailIdx'], group['headIdx']
                        return int(group['people'] ** 2)

                    # 점수 계산
                    nth = 0
                    rightIdx = (group['tailIdx'] + 1) % group['length']  # 헤더 오른쪽의 인덱스
                    if group['sequence'][rightIdx] == 2  : # -> 방향일 때
                        start = idx
                        cnt = 1
                        while start != group['headIdx']:
                            cnt += 1
                            start = (start + 1) % group['length']
                        nth = cnt
                    else: # <- 방향일 때
                        start = idx
                        cnt = 1
                        while start != group['headIdx']:
                            cnt += 1
                            start = (start + group['length'] - 1) % group['length']
                        nth = cnt

                    # 머리 꼬리 교체
                    temp = group['sequence'][group['headIdx']]  # 헤드값
                    group['sequence'][group['headIdx']] = group['sequence'][group['tailIdx']]
                    group['sequence'][group['tailIdx']] = temp
                    group['headIdx'], group['tailIdx'] = group['tailIdx'] , group['headIdx']
                    return int(nth ** 2)

        x += dx
        y += dy

    return 0


if __name__ == '__main__':
    n, m, k = map(int, input().split()) # n : 격자크기 , m : 팀의개수, k : 라운드수
    graph = [list(map(int, input().split())) for _ in range(n)]
    groups = []
    ballInfo = {} # n트 : (시작x,시작y,dx,dy)
    score = 0

    init()

    for trial in range(1, k + 1):
        move()
        score += getScore(trial)

    print(score)