from itertools import combinations_with_replacement

def solution(n, info):
    rionShot=[-1]
    apeach=info
    scoreDiffer=0

    for rionShotIdx in list(combinations_with_replacement([x for x in range(11)],n)): # 뭘 맞출지 모르니 중복조합
        rion = [0] * 11
        rionScore=0
        appeachScore=0

        for idx in rionShotIdx: # 라이언 이 쏜대로 rion 업데이트
            rion[idx]+=1

        for i in range(11): # 점수 계산
            if rion[i]== apeach[i]==0:
                continue
            if apeach[i]>=rion[i]:
                appeachScore+=10-i
            else:
                rionScore+=10-i

        if rionScore>appeachScore: # 라이언이 우승할 수 있는 경우
            if rionScore-appeachScore >= scoreDiffer:
                if rionScore-appeachScore>scoreDiffer: #새롭게 갱신
                    scoreDiffer=rionScore-appeachScore
                    rionShot=rion

                else: # 이미 기존 값이 있을 때에는 작은 점수 개수가 많은애로 갱신
                    for j in range(10,-1,-1):
                        if rion[j] == rionShot[j]:
                            continue
                        if rion[j]> rionShot[j]: #새로운 방식으로 갱신
                            rionShot=rion
                            break
                        else:
                            break

    return rionShot