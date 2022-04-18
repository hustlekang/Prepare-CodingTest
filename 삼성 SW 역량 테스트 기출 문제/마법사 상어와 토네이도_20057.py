N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

outSandAmount=0 # 밖으로 나간 모래
sand={'l':(0,-1),'r':(0,1),'u':(-1,0),'d':(1,0)} # 방향에 따른 현재 토네이도 위치에서 모래가 있는 위치까지 dx,dy
alpha={'l':(0,-2),'r':(0,2),'u':(-2,0),'d':(2,0)} # 방향에 따른 현재 토네이도 위치에서 α칸이 있는 위치까지 dx,dy
# 왼쪽 방향일 때 현재 토네이도 위치에서 모래가 채워지는 (dx,dy,비율)
areas_L=[(-1,-2,0.1),(1,-2,0.1),(-1,-1,0.07),(1,-1,0.07),(0,-3,0.05),(-2,-1,0.02),(2,-1,0.02),(-1,0,0.01),(1,0,0.01)]
areas_R=[]
areas_U=[]
areas_D=[]

for area in areas_L: # 진행 방향에 따라 좌표 값 반전 시켜준다
    x=area[0]
    y=area[1]
    percent=area[2]
    areas_R.append((x,-y,percent))
    areas_D.append((-y,x,percent))
    areas_U.append((y,-x,percent))

areaByDirection={'l':areas_L,'r':areas_R,'u':areas_U,'d':areas_D}

def spreadSand(x,y,direction,graph):
    global outSandAmount
    sand_dx,sand_dy=sand[direction]
    amount = graph[x + sand_dx][y + sand_dy] # 현재 모래의 양
    totalAmount = graph[x + sand_dx][y + sand_dy] # 전체 모래의 양

    if graph[x+sand_dx][y+sand_dy]>=10: # 모래가 10 이상이어야 주변에 채워지는 모래가 발생, 최대 percent는 10%니 10보다 커야 최소 1 발생
        for block in areaByDirection[direction]:
            dx,dy,percent=block
            nx=x+dx
            ny=y+dy
            amount -= int(totalAmount * percent) # 이동되는 모래만큼 빼준다
            if 0<=nx<N and 0<=ny<N: # 그래프 안의 영역이면 이동되는 만큼 모래를 더해주고
                graph[nx][ny]+=int(totalAmount*percent)
            else: # 그래프 밖의 영역이면 밖으로 나가는 모래임
                outSandAmount+=int(totalAmount*percent)

    alpha_dx, alpha_dy = alpha[direction]
    if 0<=x+alpha_dx<N and 0<=y+alpha_dy<N: # 남는 모래가 쌓이는 α칸의 위치가 그래프 안의 영역이면
        graph[x+alpha_dx][y+alpha_dy]+=amount # α칸에 남은만큼 더해주고
    else: # 그래프 밖의 영역이면 밖으로 나가는 모래
        outSandAmount+=amount
    graph[x + sand_dx][y + sand_dy]=0 # 원래 모래가 있던 곳은 다 이동되고 0

    return (x+sand_dx,y+sand_dy) # 토네이도가 이동된 다음 칸을 반환

tornado=(N//2,N//2,'l')
leftTop=(N//2,N//2) # 이 위치에 오면 아래로 진행방향 꺽임
k=0 # 이동하기 위한 일반항에 필요한 k값
# 토네이도 진행방향 로직은
# leftTop칸에서 왼쪽으로 한칸 이동 -> 아래로 2k-1칸 이동 -> 오른쪽으로 2k칸 이동 -> 위로 2k칸 이동 -> 왼쪽으로 2k칸 이동
while (tornado[0],tornado[1])!=(0,0):
    x,y,direction=tornado

    if (x,y)==leftTop: # 왼쪽으로 한칸 이동 후 진행 방향 아래로 꺽는다
        k+=1
        nx,ny=spreadSand(x,y,direction,graph)
        tornado=(nx,ny,'d')
        leftTop=(leftTop[0]-1,leftTop[1]-1) # 왼쪽 이동 후 아래로 꺽이는 좌표 갱신

    elif direction=='d':
        for _ in range(int(2*k-1)): # 2k-1번 만큼 아래로 이동하고 오른쪽으로 진행방향 바꿈
            x, y, direction = tornado
            nx, ny = spreadSand(x, y, direction, graph)
            tornado = (nx, ny, 'd')
        tornado=(tornado[0],tornado[1],'r') # 오른쪽으로 꺽고

    elif direction=='r':
        for _ in range(int(2*k)): # 2k번 오른쪽으로 이동 후 위로 방향 바꿈
            x, y, direction = tornado
            nx, ny = spreadSand(x, y, direction, graph)
            tornado = (nx, ny, 'r')
        tornado=(tornado[0],tornado[1],'u') # 위로 꺽고

    elif direction=='u':
        for _ in range(int(2*k)): # 2k번 위로 이동 후 왼쪽으로 방향 체인지
            x, y, direction = tornado
            nx, ny = spreadSand(x, y, direction, graph)
            tornado = (nx, ny, 'u')
        tornado=(tornado[0],tornado[1],'l') # 왼쪽으로 방향 체인지

    else: # direction=='l' 일 때
        for _ in range(int(2*k)):
            x, y, direction = tornado
            nx, ny = spreadSand(x, y, direction, graph)
            tornado = (nx, ny, 'l')

print(outSandAmount)