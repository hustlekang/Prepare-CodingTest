#시간을 정해 놓고 그 시간안에 목표치를 옮길 수 있는지 없는지 판단해서 이분탐색으로 시간을 조절
def solution(a, b, g, s, w, t):
    targetGold,targetSilver,gold,silver,maxQ,time = a,b,g,s,w,t
    cityNum=len(gold)
    start = 0
    end = 10**15
    answer=end #충분히 큰수
    while(start<=end):
        nowGold = 0
        nowSilver = 0
        nowTotal = 0
        mid = (start+end)//2

        for city in range(cityNum):
            carryCnt = mid//(time[city]*2) #왔다갔다 해야되니 t*2
            if mid % (time[city]*2) >= time[city]: #마지막엔 돌아올 필요 없으니 >=t이면 한번 더 가능
                carryCnt+=1
            maxQuantity = carryCnt * maxQ[city]
            nowGold += min(gold[city],maxQuantity) #최대치를 넘기면 최대치 까지만 옮길 수 있음
            nowSilver += min(silver[city],maxQuantity)
            nowTotal += min(gold[city]+silver[city],maxQuantity)

        if nowGold>=targetGold and nowSilver>=targetSilver and nowTotal>=targetGold+targetSilver:
            answer=min(answer,mid)
            end=mid-1
        else:
            start =mid+1

    return answer

#시간초과
# import copy
# def solution(a, b, g, s, w, t):
#     global maxQ,targetGold,targetSilver,gold,silver,time,nowGold,nowSilver
#     maxQ=w
#     silver=s
#     gold=g
#     time=t
#     timeFix=copy.deepcopy(time)
#     targetGold = a
#     targetSilver = b
#     nowGold=0
#     nowSilver=0
#     clock=1
#     while True:
#         if targetSilver<=nowSilver and targetGold<=nowGold:
#             clock -=1
#             break
#         for city in range(len(time)):
#             if clock==time[city]:
#                 carry(city)
#                 time[city] += timeFix[city]*2
#         clock+=1
#
#     return clock
#
# def carry(city):
#     global nowGold,nowSilver
#     if gold[city] ==0 and silver[city]==0:
#         return
#     plusGold=0
#     plusSilver=0
#     maxQuantity=maxQ[city]
#     if targetGold-nowGold > 0 and gold[city]>0: #금이 부족하고,보유량이 있을 시에만
#         if maxQuantity >= targetGold-nowGold: #최대 이동 용량>= 필요용량
#             plusGold= targetGold-nowGold #필요한 만큼만 옮긴다
#         else:
#             plusGold=maxQuantity  #더 필요하지만 한번에 용량제한이 있으므로 은은 못옮김
#
#     maxQuantity -= plusGold
#     nowGold+=plusGold
#     gold[city] -= plusGold
#     if targetSilver-nowSilver > 0 and silver[city]>0 and maxQuantity>0: #은이 부족하고, 보유량이 있고, 이동가능량이 있을 때
#         if maxQuantity >= targetSilver-nowSilver:
#             plusSilver=targetSilver-nowSilver
#         else:
#             plusSilver=maxQuantity
#
#     nowSilver +=plusSilver
#     silver[city] -=plusSilver