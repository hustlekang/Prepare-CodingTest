import math

def solution(fees, records):
    totalTime = {}
    inOutRecord = {}
    answer = []

    for record in records:
        time, car, type = record.split(' ')
        if type == 'IN':  # 입차
            inOutRecord[car] = time
        else:  # 출차
            timeIn = inOutRecord[car]
            in_minute = 60 * int(timeIn.split(':')[0]) + int(timeIn.split(':')[1])
            out_minute = 60 * int(time.split(':')[0]) + int(time.split(':')[1])
            del inOutRecord[car]
            if car in totalTime.keys():
                totalTime[car] += out_minute - in_minute
            else:
                totalTime[car] = out_minute - in_minute

    for leftcar in inOutRecord.keys():
        in_minute = 60 * int(inOutRecord[leftcar].split(':')[0]) + int(inOutRecord[leftcar].split(':')[1])
        out_minute = 23 * 60 + 59
        if leftcar in totalTime.keys():
            totalTime[leftcar] += out_minute - in_minute
        else:
            totalTime[leftcar] = out_minute - in_minute

    for car in sorted(totalTime.keys()):
        if totalTime[car] <= fees[0]:  # 기본 시간 이하시 기본요금
            charge = fees[1]
        else:
            charge = fees[1] + int(math.ceil((totalTime[car] - fees[0]) / fees[2]) * fees[3])

        answer.append(charge)

    return answer