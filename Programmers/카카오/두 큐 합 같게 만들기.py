from collections import deque

def devidable(queue, sum):
    total = sum / 2
    maxIdx = len(queue)
    end = 0
    partSum = 0
    for start in range(len(queue)):
        while (partSum < total and end < maxIdx):
            partSum += queue[end]
            end += 1
        if partSum == total:
            return True
        partSum -= queue[start]
    return False

def modify(queue1, queue2, sum1, sum2):
    cnt = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    while sum1 != sum2:
        if sum1 > sum2:
            num = q1.popleft()
            sum1 -= num
            sum2 += num
            q2.append(num)
        else:
            num = q2.popleft()
            sum2 -= num
            sum1 += num
            q1.append(num)

        cnt += 1

    return cnt

def solution(queue1, queue2):
    answer = -1
    total1 = sum(queue1)
    total2 = sum(queue2)

    if devidable(queue1 + queue2, total1 + total2) == False:
        return answer

    answer = modify(queue1, queue2, total1, total2)
    return answer