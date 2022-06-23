from collections import defaultdict
import sys

def convertToSec(time):
    h,m=time.split(':')
    return int(h)*60 + int(m)

S,E,Q=sys.stdin.readline().strip().split(' ')
start = convertToSec(S)
end = convertToSec(E)
quit = convertToSec(Q)
answer=0
dic=defaultdict(list)

while True:
    line=sys.stdin.readline().strip()
    if not line:
        break
    time,nickname=line.split(' ')
    dic[nickname].append(convertToSec(time))

for nickname in dic.keys():
    if len(dic[nickname]) < 2:
        continue

    logs=sorted(dic[nickname])
    index=-1
    for i in range(len(logs)):
        if logs[i]<=start: # 개총 시작 전에 채팅 기록이 있는지 확인
                index=i
                break
    if index == -1: # 개총 시작 전 기록이 없다면 스킵
        continue

    for i in range(index,len(logs)):
        if end<=logs[i]<=quit: # 개총끝 ~ 스트리밍 끝
            answer+=1
            break
    else:
        continue

print(answer)