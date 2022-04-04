def solution(m, n, board):
    graph = []
    cnt = 0
    for line in board:
        graph.append(list(line))

    willErase = []
    while True:
        for col in range(m - 1):
            for row in range(n - 1):
                if graph[col][row] == graph[col][row + 1] == graph[col + 1][row] == graph[col + 1][row + 1]:
                    if graph[col][row] == -1: #-1은 블록이 아래로 이동되고 빈 곳
                        continue
                    willErase.append((col, row))

        if len(willErase) == 0: #제거할 블록 없으면 종료
            break

        for i in willErase:
            x = i[0]
            y = i[1]
            if graph[x][y] != 0:
                graph[x][y] = 0
                cnt += 1
            if graph[x][y + 1] != 0:
                graph[x][y + 1] = 0
                cnt += 1
            if graph[x + 1][y] != 0:
                graph[x + 1][y] = 0
                cnt += 1
            if graph[x + 1][y + 1] != 0:
                graph[x + 1][y + 1] = 0
                cnt += 1

        willErase = []

        for row in range(n):
            line = [i[row] for i in graph] #세로줄
            if 0 not in line:
                continue
            for _ in range(line.count(0)): #0제거
                line.remove(0)
            line=line[::-1] #뒤집어서
            for _ in range(m - len(line)):
                line.append(-1) #이동된 부분은 -1로 표시
            line = line[::-1] #다시 뒤집

            for col in range(m): #아래로 당김
                graph[col][row] = line[col]

    return cnt