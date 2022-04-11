from collections import deque

def solution(n, t, m, timetable):
    maxPerson=m
    answer=0
    left = 1
    right = 1439
    while left <= right:
        waiting = []
        for time in timetable:
            h,m=map(int,time.split(":"))
            waiting.append((h*60+m, -1))

        mid = (left + right) // 2
        arrivedTime = mid

        waiting.append((arrivedTime, 1))
        waiting.sort(key=lambda x: x[1])
        waiting.sort(key=lambda x: x[0])

        queue=deque(waiting)
        time=540
        for trial in range(n): #n번 동안 큐에 대기중인 사람들을 태워 나른다
            ride=0
            while queue[0][0]<=time:
                queue.popleft()
                ride+=1
                if ride==maxPerson:
                    break
            time += t

        if (arrivedTime,1) in queue: #회사에 못가고 줄에 서있는중
            right=mid-1 # 줄서는 시간을 좀더 앞당긴다
        else:
            left=mid+1 # 회사도착, 좀더 늦게 나와보자
            answer=max(answer,arrivedTime)

    hour=answer//60
    minute=answer%60
    if hour<10:
        hour=('0'+str(hour))
    else:
        hour=str(hour)

    if minute<10:
        minute=('0'+str(minute))
    else:
        minute=str(minute)

    answer=hour+':'+minute
    return answer