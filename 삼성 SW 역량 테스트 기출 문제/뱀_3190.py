from collections import deque

N=int(input())
K=int(input())
graph=[[0]*N for _ in range(N)]
changeDirectionTime={}
direction={ # 현재 바라보고 있는 방향에 따른 다음 칸
    'u':(-1,0),
    'd':(1,0),
    'l':(0,-1),
    'r':(0,1)
}
changeDirection={ # 현재 바라보는 방향에 따른 왼쪽과 오른쪽의 새로운 방향
    'u':{'L':'l','D':'r'},
    'd':{'L':'r','D':'l'},
    'r':{'L':'u','D':'d'},
    'l':{'L':'d','D':'u'}
}
for _ in range(K): #사과 위치 기록
    x,y=map(int,input().split())
    graph[x-1][y-1]=1

L=int(input())
for _ in range(L): #방향 바꾸는 시간 기록
    sec,way=input().split()
    changeDirectionTime[int(sec)]=way

way='r'
snake=deque([(0,0)])
t=0
while True:
    if t in changeDirectionTime.keys():
        way=changeDirection[way][changeDirectionTime[t]]

    dx,dy=direction[way]
    nx=snake[-1][0]+dx
    ny=snake[-1][1]+dy
    if (nx<0 or N<=nx) or (ny<0 or N<=ny) or (nx,ny) in snake: # 밖으로 나가거나 or 자기자신과 만나면
        t+=1
        break
    else:
        t+=1
        snake.append((nx,ny)) #이동할 때 머리부분 앞에만 추가해주고, 꼬리부분 맨 뒤에를 빼주면 된다
        if graph[nx][ny]==1: #사과가 있으면
            graph[nx][ny]=0 # 꼬리부분을 빼줄 필요x, 사과만 사용
        else:
            snake.popleft() # 꼬리쪽 빼버림

print(t)