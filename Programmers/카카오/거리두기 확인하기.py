from collections import deque

def solution(places):
    answer = []
    for place in places:  # 대기실별로 체크
        person = [] # 사람있는 위치 좌표 (x,y)
        isOk = True # 거리두기 잘 하고 있나
        for i in range(5):  # person 초기화
            for j in range(5):
                if place[i][j] == 'P':
                    person.append((i, j))

        if len(person) == 0:  # 사람이 없으면 볼 필요 x
            answer.append(1)
            continue

        for p in person:
            visit = [[False] * 5 for _ in range(5)]
            visit[p[0]][p[1]] = True
            queue = deque([(p, 0)])

            while queue:
                node, distance = queue.popleft()
                x, y = node

                if place[x][y] == 'P' and (x, y) != p:
                    if distance <= 2: # 다른 사람과의 거리가 2 이하면
                        isOk = False # 불가능
                        break
                    continue

                for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and visit[nx][ny] == False and place[nx][ny] != 'X':
                        visit[nx][ny] = True
                        queue.append(((nx, ny), distance + 1))
            if not isOk:
                break

        if isOk:
            answer.append(1)
        else:
            answer.append(0)

    return answer