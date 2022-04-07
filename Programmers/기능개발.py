from collections import deque

def solution(progresses, speeds):
    works = []
    for progress, speed in zip(progresses, speeds):
        works.append([progress, speed])
    queue = deque(works)
    answer = []
    day = 0
    cnt = 0
    while queue:
        progress, speed = queue.popleft()
        if (progress + speed * day) >= 100: #현재 day기준 작업량이 100이상이면
            cnt += 1 #가능한 작업 늘려준다
        else: #현재 day기준 큐에서 뽑은 일이 완료가 안됐으면
            if cnt != 0: # 완료된 작업은 answer에 넣어주고
                answer.append(cnt)
            need = (100 - (progress + speed * day)) // speed #완료를 위해 필요한 기간
            if (100 - (progress + speed * day)) % speed != 0: #나머지 있으면 하루 추가
                need += 1
            day += need #day는 지금 작업이 완료된 날로 증가
            cnt = 1 # 가능한 작업은 방금 처리한 1개로 초기화

    answer.append(cnt)

    return answer