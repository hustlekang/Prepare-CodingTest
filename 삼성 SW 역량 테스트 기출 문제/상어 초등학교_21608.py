N=int(input())
total_satisfiedScore=0
classroom=[[0]*N for _ in range(N)]
studentFavorite={} # 학생별 좋아하는 친구
directionX=[0,0,-1,1]
directionY=[1,-1,0,0]

for _ in range(N**2):
    line=list(map(int,input().split()))
    studentFavorite[line[0]]=line[1:]

for student in studentFavorite.keys():
    firstDecision=[] # 첫번째 조건을 만족하는 자리
    max_cnt_favoriteFriend=0
    for x in range(N):
        for y in range(N):
            if classroom[x][y]==0:
                cnt_favoriteFriend=0 # 칸 주변에 좋아하는 친구 수
                for dx,dy in zip(directionX,directionY):
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<N and 0<=ny<N and classroom[nx][ny] in studentFavorite[student]:
                        cnt_favoriteFriend+=1

                if max_cnt_favoriteFriend<=cnt_favoriteFriend:
                    if max_cnt_favoriteFriend==cnt_favoriteFriend:
                        firstDecision.append((x,y))
                    else:
                        max_cnt_favoriteFriend=cnt_favoriteFriend
                        firstDecision=[(x,y)]

    if len(firstDecision)==1:
        classroom[firstDecision[0][0]][firstDecision[0][1]]=student

    else: # 첫번째 조건 만족 자리가 여러개이면
        secondDecision=[] # 두번째 조건 만족 자리
        max_cnt_emptySeat=0
        for seat in firstDecision: # 1번 조건 가능한 칸들중에서
            cnt_emptySeat = 0
            for dx,dy in zip(directionX,directionY):
                nx=seat[0]+dx
                ny=seat[1]+dy
                if 0<=nx<N and 0<=ny<N and classroom[nx][ny]==0:
                    cnt_emptySeat+=1

            if max_cnt_emptySeat<=cnt_emptySeat:
                if max_cnt_emptySeat==cnt_emptySeat:
                    secondDecision.append(seat)
                else:
                    max_cnt_emptySeat=cnt_emptySeat
                    secondDecision=[seat]

        if len(secondDecision)==1:
            classroom[secondDecision[0][0]][secondDecision[0][1]]=student

        else: # 두번째 조건 만족 자리도 여러개 이면
            secondDecision.sort(key=lambda x:x[1])
            secondDecision.sort(key=lambda x:x[0])
            classroom[secondDecision[0][0]][secondDecision[0][1]]=student

for x in range(N):
    for y in range(N):
        student=classroom[x][y]
        cnt_favorite=0
        for dx,dy in zip(directionX,directionY):
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<N and classroom[nx][ny] in studentFavorite[student]:
                cnt_favorite+=1

        if cnt_favorite==0:
            total_satisfiedScore+=0
        elif cnt_favorite==1:
            total_satisfiedScore+=1
        elif cnt_favorite==2:
            total_satisfiedScore+=10
        elif cnt_favorite==3:
            total_satisfiedScore+=100
        else:
            total_satisfiedScore+=1000

print(total_satisfiedScore)