from collections import deque

H, W = map(int,input().split())
heights = list(map(int,input().split()))
rainBlock=0
queue=deque()
graph = [[0]*W for _ in range(H)] # 0 : 빈 공간, -1 : 벽

for height,i in zip(heights,range(W)):
    for j in range(height):
        graph[H-1-j][i]=-1

for i in range(H-1,-1,-1): # 바닥부터 위로 물을 채운다
    visit=[False]*W
    for j in range(W):
        if graph[i][j] == 0 and not visit[j]:
            visit[j]=True
            queue.append([j])
            while queue:
                v=queue.popleft()
                if v[-1]+1<W and graph[i][v[-1]+1] == 0: # 빈 공간을 계속 찾아주고
                    visit[v[-1]+1]=True
                    queue.append(v+[v[-1]+1])
                else: # 다 찾으면
                    left =v[0] # 제일 왼쪽부분 인덱스
                    right=v[-1] # 제일 오른쪽 인덱스

                    # 맨 왼쪽과 맨 오른쪽 바깥 부분이 벽으로 막혀 있나 확인
                    # 1층 아래는 막혀있고 (문제에서), 아래 부터 위로 빈 공간은 다 벽으로 메꾸기 때문에 바닥이 막혀있는지 체크할 필요X
                    if  0<=left-1 and right+1<W and graph[i][left-1]== -1 and graph[i][right+1]==-1:
                        rainBlock+=len(v) # 빈 공간 만큼 카운트 해주고
                        for idx in v: # 공간을 다 벽으로 메꿔버림 -> 다음 층 계산을 위해
                            graph[i][idx]=-1

print(rainBlock)