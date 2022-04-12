# pypy3
from collections import deque

N,K=map(int,input().split())
durabilities=list(map(int,input().split()))
belt=deque([])
trial=1

for durability in durabilities:
    belt.append([durability,[]])

while True:
    belt.rotate(1)
    if belt[N-1][1]: # 내리는 위치에 오면 바로 빼준다
        belt[N-1][1].pop()

    robotExist=[] # [[인덱스,언제 올라온 로봇인지]...]
    for i in range(len(belt)):
        if belt[i][1]: #로봇의 위치를 기록
            robotExist.append((i,belt[i][1][0]))

    robotExist.sort(key=lambda x:x[1]) #먼저 올라온 로봇 순으로 정렬

    for robot in robotExist: # 로봇 이동
        nextIdx=int((robot[0]+1)%(2*N))
        if not belt[nextIdx][1] and belt[nextIdx][0]>0: # 로봇이 없고 내구도가 0보다 클 때
            v=belt[robot[0]][1].pop() #원래 위치에서 빼서
            belt[nextIdx][1].append(v) #이동해주고
            belt[nextIdx][0]-=1 # 내구도 -1

    if belt[N-1][1]: # 내리는 위치에 오면 바로 빼준다
        belt[N-1][1].pop()

    if belt[0][0]>0: #올리는 위치에 올릴수 있으면 로봇 올리기
        belt[0][1].append(trial)
        belt[0][0]-=1 # 내구도 -1

    cnt=0
    for each in belt:
        if each[0]==0:
            cnt+=1

    if cnt>=K:
        break

    trial+=1

print(trial)