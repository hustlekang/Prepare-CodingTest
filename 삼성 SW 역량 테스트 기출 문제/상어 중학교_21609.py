from collections import deque

N,M=map(int,input().split())
graph=[]
score=0
for _ in range(N):
    graph.append(list(map(int,input().split())))

def rotate_90(graph,N):
    rotated=[]
    for i in range(N):
        rotated.append([row[N-1-i] for row in graph])
    return rotated

directionX=[0,0,-1,1]
directionY=[1,-1,0,0]

while True:
    blockGroups=[]
    deleteBlock=None
    maxBlockGroupSize=2
    visit=[[False]*N for _ in range(N)]
    queue=deque([])
    for x in range(N):
        for y in range(N):
            if visit[x][y]==False and (graph[x][y] not in (-1,0,-2)): #일반 블록일때만 카운팅, -2:블록 있다 제거된 부분
                color=graph[x][y] # 일반 블록은 무조건 색깔이 같아야함
                blockGroupSize=1
                rainbowCnt=0 # 무지개 블록 개수
                standard=(x,y) # 기준블록 초기 세팅
                coordinates=[(x,y)]
                coordinates_rainbow=[]

                queue.append((x,y))
                visit[x][y]=True

                while queue:
                    r,c=queue.popleft()
                    for dx,dy in zip(directionX,directionY):
                        nr = r + dx
                        nc = c + dy

                        if 0<=nr<N and 0<=nc<N and visit[nr][nc]==False and (graph[nr][nc]==0 or graph[nr][nc]==color):
                            if graph[nr][nc]==0: # 무지개 블록이면
                                rainbowCnt+=1
                                coordinates_rainbow.append((nr,nc))

                            else: #색깔 같은 블록이면 기준 블록 갱신
                                if nr<=standard[0]:
                                    if nr==standard[0]: # 행 번호가 같으면 열이 더 작아야 갱신
                                        if nc<standard[1]:
                                            standard=(nr,nc)
                                    else:
                                        standard =(nr,nc)

                            visit[nr][nc]=True
                            blockGroupSize+=1
                            queue.append((nr,nc))
                            coordinates.append((nr,nc))

                for rainbowBlock in coordinates_rainbow: # 무지개 블록 영역은 누구나 참조가 가능하니 방문처리 초기화
                    visit[rainbowBlock[0]][rainbowBlock[1]]=False

                if blockGroupSize>=maxBlockGroupSize: # 블록개수가 최대값 보다 크거나 같을 때 갱신
                    if blockGroupSize==maxBlockGroupSize:
                        blockGroups.append((blockGroupSize,coordinates,rainbowCnt,standard))
                    else: # 새롭게 최대값 갱신
                        blockGroups=[(blockGroupSize,coordinates,rainbowCnt,standard)]
                        maxBlockGroupSize=blockGroupSize

    if len(blockGroups)==0: # 블록 그룹이 없으면 오토 플레이 종료
        break

    else: # 1단계 실행
        blockGroups.sort(key=lambda x:x[3][1],reverse=True)
        blockGroups.sort(key=lambda x:x[3][0],reverse=True)
        blockGroups.sort(key=lambda x:x[2],reverse=True)
        deleteBlock=blockGroups[0] # (blockGroupSize,coordinates,rainbowCnt,standard)

        # 2단계 실행
        for block in deleteBlock[1]:
            graph[block[0]][block[1]]=-2 # -2는 빈공간

        score+=deleteBlock[0]**2

        # 3단계 실행
        for x in range(N-1,-1,-1): # 맨 아랫줄 부터 아래로 떨궈야 됨
            for y in range(N):
                if graph[x][y] not in (-1,-2): # 검정색 블록과 빈공간 제외
                    nx=x
                    while nx<N-1:
                        if graph[nx+1][y]==-2:
                            nx+=1
                        else:
                            break

                    if x!=nx:
                        graph[nx][y]=graph[x][y]
                        graph[x][y]=-2

        # 4단계 실행
        graph=rotate_90(graph,N)

        #5단계 실행
        for x in range(N-1,-1,-1): # 맨 아랫줄 부터 아래로 떨궈야 됨
            for y in range(N):
                if graph[x][y] not in (-1,-2): # 검정색 블록과 빈공간 제외
                    nx=x
                    while nx<N-1:
                        if graph[nx+1][y]==-2:
                            nx+=1
                        else:
                            break

                    if x!=nx:
                        graph[nx][y]=graph[x][y]
                        graph[x][y]=-2

print(score)