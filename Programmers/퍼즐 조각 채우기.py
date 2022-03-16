# 블록을 회전할 때, 인덱스 쉽게 주려고 무조건 정방형으로 만든 뒤 했는데 테스트케이스 4개 통과 못해서
# 그냥 블록 사이즈 대로 회전 시키니 통과
def solution(game_board, table):
    global n
    graph=game_board
    graph_table=table
    n = len(game_board)
    visit=[[False]*n for _ in range(n)]
    visit_table=[[False]*n for _ in range(n)]
    answer=0
    emptySpace=[] # 빈 공간을 구성하는 좌표들
    emptyFinal=[] # 최종적인 빈공간 블록 모양
    blockSpace=[] # 블록을 구성하는 좌표들
    blockFinal=[] # 최종적인 블록 모양

    for i in range(n): # 빈 공간인 영역의 좌표값 구해줌
        for j in range(n):
            if graph[i][j]==0 and visit[i][j]==False:
                coordinate=[]
                dfs(i,j,visit,graph,coordinate,0)
                emptySpace.append(coordinate)

    for section in emptySpace: # 좌표값들로 실제 블록 모양을 구함
        maxX=max(i[0] for i in section)
        minX=min(i[0] for i in section)
        maxY=max(i[1] for i in section)
        minY=min(i[1] for i in section)
        temp=graph[minX:maxX+1]

        for line in range(len(temp)):
            temp[line]=temp[line][minY:maxY+1]

        emptyFinal.append(temp)

    for i in range(n): # 블록 영역 좌표값 구하고
        for j in range(n):
            if graph_table[i][j] == 1 and visit_table[i][j] == False:
                coordinate=[]
                dfs(i, j, visit_table, graph_table, coordinate,1)
                blockSpace.append(coordinate)

    for block in blockSpace: # 실제 블록 모양으로
        maxX = max(i[0] for i in block)
        minX = min(i[0] for i in block)
        maxY = max(i[1] for i in block)
        minY = min(i[1] for i in block)
        temp = graph_table[minX:maxX + 1]

        for line in range(len(temp)):
            temp[line] = temp[line][minY:maxY + 1]

        for i in range(len(temp)): # 빈공간과 블록이 같은지 따질 것이기 때문에 1과 0을 반전 시킴
            for j in range(len(temp[0])):
                if temp[i][j]==0:
                    temp[i][j]=1
                else:
                    temp[i][j]=0
        blockFinal.append(temp)

    for empty in emptyFinal: # 모든 빈 공간에 대해
        for rotated in rotate(empty): # 회전한 4가지 블록들 중
            if rotated in blockFinal: # 한개라도 있으면
                cnt=0
                for x in range(len(rotated)):
                    for y in range(len(rotated[0])):
                        if rotated[x][y]==0: #블록의 내부 영역 개수 세주고
                            cnt+=1

                answer+=cnt #정답에 더한다

                blockFinal.remove(rotated) #중복해서 사용하면 안되니까 제거
                break

    return answer

def dfs(x,y,visit,graph,coordinate,target):
    visit[x][y]=True
    coordinate.append((x,y))
    directionX = [0, 0, -1, 1]
    directionY = [1, -1, 0, 0]
    for dx, dy in zip(directionX, directionY):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == False and graph[nx][ny] == target:
            dfs(nx,ny,visit,graph,coordinate,target)

def rotate(array):
    x= len(array)
    y= len(array[0])
    right_90 = [[0] * x for _ in range(y)]
    right_180 = [[0] * y for _ in range(x)]
    right_270 = [[0] * x for _ in range(y)]

    for i in range(x):
        for j in range(y):
            right_90[j][x-1-i]=array[i][j]
            right_180[x-1-i][y-1-j]=array[i][j]
            right_270[y-1-j][i]=array[i][j]

    return [array,right_90,right_180,right_270]