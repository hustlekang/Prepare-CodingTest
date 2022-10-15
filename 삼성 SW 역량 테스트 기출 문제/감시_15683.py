info = {
        1 : [
            [(-1, 0)],
            [(1,0)],
            [(0,-1)],
            [(0,1)]
        ],
        2 : [
            [(0,-1),(0,1)],
            [(-1,0),(1,0)]
        ],
        3 : [
            [(-1, 0), [0, 1]],
            [(1,0),(0,1)],
            [(0,-1),(1,0)],
            [(-1,0),(0,-1)]
        ],
        4 : [
            [(-1,0),(0,1),(1,0)],
            [(0,1),(1,0),(0,-1)],
            [(1,0), (0,-1), (-1,0)],
            [(0,-1), (-1,0), (0,1)]
        ],
        5 : [
            [(-1,0),(0,1),(1,0),(0,-1)]
        ]
    }


def product(arrs):
    result = [[]]
    for arr in arrs:
        result = [x + [y] for x in result for y in arr]
    return result


def solution(indexes):
    global cctv, N, M, wall, info

    catchSpots = set()

    for j , i in zip(cctv,indexes):
        x, y, no = j
        cnt = 0
        temp = set()
        for dx, dy in info[no][i]:
            nx ,ny = x, y
            while True:
                nx += dx
                ny += dy

                if nx < 0 or N <= nx or ny < 0 or M <= ny:
                    break
                if graph[nx][ny] == 6:
                    break
                if graph[nx][ny] == 0:
                    temp.add((nx,ny))
                    cnt += 1

        catchSpots |= temp

    blindSpot = int(N * M) - len(catchSpots) - len(cctv) - wall

    return  blindSpot


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    cctv = [] # (x,y,종류)
    wall = 0

    for i in range(N):
        for j in range(M):
            if 1 <= graph[i][j] <= 5:
                cctv.append((i,j, graph[i][j]))
            elif graph[i][j] == 6:
                wall += 1

    arr = []
    for x,y,t in cctv:
        arr.append([x for x in range(len(info[t]))])

    answer = 100
    for indexes in product(arr):
        answer= min(answer, solution(indexes))

    print(answer)