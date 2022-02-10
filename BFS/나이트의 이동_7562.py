from collections import deque
directionX=[-2,-2,-1,1,2,2,1,-1]
directionY=[-1,1,2,2,1,-1,-2,-2]
trial=int(input())
answerList=[]
for _ in range(trial):
    m=int(input())
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    start=[a,b]
    end=[c,d]
    answer=None
    visit=[[False]*m for _ in range(m)]
    queue=deque([[start[0],start[1],0]])
    visit[start[0]][start[1]]=True

    while(queue):
        x,y,distance=queue.popleft()
        if (x,y)==(end[0],end[1]):
            answer=distance
            answerList.append(answer)
            break

        for dx,dy in zip(directionX,directionY):
            nx=x+dx
            ny=y+dy
            if 0<=nx<m and 0<=ny<m and visit[nx][ny]==False:
                queue.append([nx,ny,distance+1])
                visit[nx][ny]=True

for answer in answerList:
    print(answer)