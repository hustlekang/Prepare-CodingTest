N,M=map(int,input().split())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
answer=0
tetrominos=[
    [(0,1),(0,2),(0,3)], #---- 2가지
    [(1,0),(2,0),(3,0)],
    [(1,0),(0,1),(1,1)], #ㅁ 1가지
    [(1,0),(2,0),(2,1)], #ㄴ 8 가지
    [(1,0),(0,1),(0,2)],
    [(0,1),(1,1),(2,1)],
    [(0,1),(0,2),(-1,2)],
    [(0,1),(-1,1),(-2,1)],
    [(0,1),(1,0),(2,0)],
    [(0,1),(0,2),(1,2)],
    [(1,0),(1,1),(1,2)],
    [(1,0),(1,1),(2,1)],   # --
    [(0,1),(-1,1),(-1,2)], #  -- 4가지
    [(1,0),(0,1),(-1,1)],
    [(0,1),(1,1),(1,2)],
    [(0,1),(0,2),(1,1)], # ㅗ 4가지
    [(1,-1),(1,0),(2,0)],
    [(1,-1),(1,0),(1,1)],
    [(1,0),(2,0),(1,1)]
]

for i in range(N):
    for j in range(M):
        x,y = i,j
        for tetromino in tetrominos:
            score=graph[x][y]
            isPossible=True
            for differ in tetromino:
                nx=x+differ[0]
                ny=y+differ[1]
                if 0<=nx<N and 0<=ny<M:
                    score+=graph[nx][ny]
                else:
                    isPossible=False
                    break
            if isPossible:
                answer=max(answer,score)

print(answer)