def changeTimeToSec(string): # 'hh:mm:ss' 를 초단위 시간으로 변경하는 함수
   h, m, s= string.split(':')
   sec = int(h)*3600 + int(m)*60 + int(s)

   return sec

def changeTimeToString(sec): # 초단위 시간을 'hh:mm:ss'로 변경하는 함수
    h = sec//3600
    sec -= h*3600
    m = sec// 60
    sec -= m*60
    time = [h,m,sec]

    for i in range(len(time)):
        if time[i] < 10:
            time[i] = '0' + str(time[i])

    stringTime = '{}:{}:{}'.format(time[0],time[1],time[2])

    return stringTime

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return '00:00:00'

    length = changeTimeToSec(play_time) + 1
    record = [0]*length # record 배열의 인덱스는 0초,1초,2초,n초를 나타냄

    # 누적합을 구하기 위해 record[시작시작]에 +1, record[끝지점+1]에 -1
    for log in logs:
        start, end = log.split('-')
        start_s = changeTimeToSec(start)
        end_s = changeTimeToSec(end)
        record[start_s] += 1
        # end[_s+1] -= 1 인데 테케 6개 틀림
        record[end_s] -= 1 # 이건 다맞음

    # 누적합으로 record 배열 갱신
    acc = 0
    for i in range(length):
        n = record[i]
        record[i] += acc
        acc += n

    # 0초부터 광고 시간에 해당하는 구간만큼 합을 구할거임
    adv_length = changeTimeToSec(adv_time)
    partSum = sum(record[0:adv_length+1]) # 초기값
    maxSum = partSum
    answer = '00:00:00'

    for i in range(1, length - adv_length):
        partSum -= record[i-1] # 1초씩 지날 때 마다 이전의 맨 앞부분 빠지고
        # partSum += record[i + adv_length]  # 마지막 하나를 덜봐야 다맞음
        partSum += record[i+adv_length-1] # 새롭게 맨 뒤에 추가됨
        if maxSum < partSum:
            answer = changeTimeToString(i)
            maxSum = partSum

    return answer