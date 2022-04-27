def msecTime(endTime, duration): #시작시간과 종료시간을 밀리초로 계산, 소수점 계산하면 오류남;
    h, m, s = endTime.split(':')
    h = int(h)
    m = int(m)
    s = round(float(s),4)
    duration = int(round(float(duration.split('s')[0]),4)*1000)
    endTimeSec = int((  (h * 60 * 60) + (m * 60) + s )*1000)
    startTime=endTimeSec-duration+1

    return [startTime,endTimeSec]

def solution(lines):
    answer=0
    data=[]
    for line in lines:
        trash, endTime, duration = line.split(' ')
        data.append(msecTime(endTime, duration))

    checkTime= sum(data,[]) # 모든 시작 시간과 종료 시간만 체크하면 됨
    for sec in checkTime:
        cnt = 0
        for each in data:
            # 시작점이 구간에 있거나, 종료점이 구간에 있거나, 아예 그 구간을 포함해버리거나
            if sec<=each[0]<=sec+999 or sec<=each[1]<=sec+999 or (each[0]<sec and sec+999<each[1]) :
                cnt+=1
        answer = max(answer, cnt)

    return answer