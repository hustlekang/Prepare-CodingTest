def isBingo(visit):
    cnt=0
    for i in range(5): # 가로줄 체크
        bingo=True
        for j in range(5):
            if visit[i][j] == False:
                bingo=False
                break
        if bingo:
            cnt+=1

    for j in range(5): # 세로줄 체크
        bingo=True
        for i in range(5):
            if visit[i][j]== False:
                bingo=False
                break
        if bingo:
            cnt+=1

    # 왼쪽 대각선
    x1,y1=0,0
    bingo=True
    for d in range(5):
        if visit[x1+d][y1+d] == False:
            bingo = False
            break

    if bingo:
        cnt+=1

    # 오른쪽 대각선
    x2,y2 = 4,0
    bingo=True
    for d in range(5):
        if visit[x2-d][y2+d] == False:
            bingo=False
            break
    if bingo:
        cnt+=1

    return cnt

answer=0
position={}
order=[]
visit=[[False]*5 for _ in range(5)]

for i in range(5):
    line=list(map(int, input().split()))
    for j in range(5):
        position[line[j]]=(i,j)

for _ in range(5):
    order+=list(map(int,input().split()))

for number,cnt in zip(order,range(1,26)):
    x,y=position[number]
    visit[x][y]=True
    if isBingo(visit) >= 3: # 3개 미만이다가 한번에 4개가 될수도 있으니
        answer=cnt
        break

print(answer)