from collections import deque

N,M,K=map(int,input().split())
answer=0
fireballs=deque([]) # 모든 파이어볼들의 정보
location={} # 키 : (r,c) , 값 : [(m,s,d)...]
moveDirection={
    0:(-1,0),
    1:(-1,1),
    2:(0,1),
    3:(1,1),
    4:(1,0),
    5:(1,-1),
    6:(0,-1),
    7:(-1,-1)
}

for _ in range(M):
    r,c,m,s,d=map(int,input().split())
    fireballs.append((r-1,c-1,m,s,d))  # 인덱스= 행렬 -1

for trial in range(K):
    for _ in range(len(fireballs)):
        r,c,m,s,d=fireballs.popleft()
        nr=(r+moveDirection[d][0]*s)%N
        nc=(c+moveDirection[d][1]*s)%N
        fireballs.append((nr,nc,m,s,d)) # 모든 파이어볼 이동

        if (nr,nc) in location.keys(): # (r,c)에 있는 파이어볼의 (m,s,d) 기록
            location[(nr,nc)].append((m,s,d))
        else:
            location[(nr,nc)]=[(m,s,d)]

    for block in location.keys():
        if len(location[block])>=2:
            sum_s=0
            sum_m=0
            remainder=location[block][0][2]%2
            isAllSame=True
            for ball in location[block]:
                sum_m+=ball[0]
                sum_s+=ball[1]
                if isAllSame==True:
                    if remainder != ball[2]%2:
                        isAllSame=False
                    else:
                        remainder=ball[2]%2

            new_s=sum_s//len(location[block])
            new_m=sum_m//5

            if new_m !=0:
                if isAllSame:
                    location[block] = [(new_m,new_s,new_d) for new_d in (0,2,4,6)]
                else:
                    location[block] = [(new_m,new_s,new_d) for new_d in (1,3,5,7)]

            else: # 질량이 0 이면 소멸
                location[block]=[]

    if trial==K-1: # 마지막 이동이 끝나면 모든 질량의 합 구해준다
        for key in location.keys():
            for each in location[key]:
                answer+=each[0]

    else:
        fireballs.clear() # 이동된 파이어볼의 정보를 업데이트
        for key in location.keys():
            for each in location[key]:
                fireballs.append((key[0],key[1],each[0],each[1],each[2]))
        location.clear() # 다음 이동 때 다시 기록해야하니 초기화

print(answer)