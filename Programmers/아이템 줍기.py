# ㅁ의 꼭지점을 좌표상에 찍으면
# 11
# 11
# ㄷ의 꼭지점을 좌표상에 찍어도
# 11
# 11
# 변을 타고 이동 해야 되기 때문에 구분이 안된다
# 모든 좌표를 2배씩 확대하면 ㄷ,ㅁ 구분 가능
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    start=(int(characterY*2),int(characterX*2))
    target=(int(itemY*2),int(itemX*2))
    directionX=[1,-1,0,0]
    directionY=[0,0,1,-1]
    graph=[[0]*102 for _ in range(102)]
    visit=[[False]*102 for _ in range(102)]
    answer = 0

    for point in rectangle:
       for x in range(int(2*point[1]),int(2*point[3])+1):
           if x==int(2*point[1]) or x==int(2*point[3]): #밑변과 윗변일 때
               for y in range(int(2*point[0]),int(2*point[2])+1):
                   if graph[x][y]!=9: # 어떤 사각형의 내부가 아니라면
                       graph[x][y]=1 # 이동가능 1
           else: # 좌변과 우변일 때
               if graph[x][int(2 * point[0])] !=9: # 어떤 사각형의 내부가 아니라면
                    graph[x][int(2 * point[0])] = 1
               if graph[x][int(2 * point[2])]!=9: # 어떤 사각형의 내부가 아니라면
                   graph[x][int(2 * point[2])] = 1
               for y in range(int(2 * point[0])+1, int(2 * point[2])): #내부는 다 9로 처리
                   graph[x][y] = 9

    queue=deque([(start[0],start[1],0)])
    visit[start[0]][start[1]]=True

    while queue:
        x,y,distance=queue.popleft()

        if x==target[0] and y==target[1]:
            answer = int(distance/2) #2배씩 확대 했으니 다시 원래로 돌림
            break

        for dx,dy in zip(directionX,directionY):
            nx = x + dx
            ny = y + dy
            if 0<=nx<102 and 0<=ny<102 and visit[nx][ny]==False and graph[nx][ny]==1:
                visit[nx][ny]=True
                queue.append((nx,ny,distance+1))

    return answer