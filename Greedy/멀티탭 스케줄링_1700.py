#플러그가 꽉 찼을 때
#플러그에 꽂혀 있는 애들 중에서 누구를 빼냐면
#앞으로 사용할 남아있는 device중 첫 사용이 가장 나중인 device를 빼준다
#앞으로 여러번 사용해도 결국 첫 사용만 보면 됨 ( 당장 사용할 것만 보면 된다 = 그리디)
#사용할 일이 없는 얘는 1000번째에 사용한다고 했음 (사용할 기기가 최대 100개임)

n, k = map(int, input().split())
sequence = list(map(int, input().split()))
plug = []
answer = 0
for deviceIdx in range(len(sequence)):
    device = sequence[deviceIdx]
    if len(plug) < n:
        if device in plug:
            continue
        plug.append(device)
    else:
        if device in plug:
            continue

        whatWillDel = []
        for alreadyDevice in plug:
            whenIdx = 1000
            idx=deviceIdx-1 #새롭게 들어갈 device의 sequence에서의 인덱스를 구하기 위한 변수
            for deviceWillAppend in sequence[deviceIdx:]:
                idx+=1
                if alreadyDevice == deviceWillAppend:
                    if whenIdx !=1000: # 가장 먼저 사용할 순서만 알면됨, whenIdx가 지정되면 그 다음번 사용 순서는 필요 없으니 스킵
                        continue
                    whenIdx=idx #가장 먼저 사용할 순서를 지정

            whatWillDel.append((alreadyDevice,whenIdx))

        whatWillDel.sort(key=lambda x: x[1],reverse=True) #맨앞에 가장 나중에 사용될 device가 위치하도록 정렬

        plug.remove(whatWillDel[0][0])
        plug.append(device)
        answer += 1

print(answer)