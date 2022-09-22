from collections import defaultdict
import heapq as h
import sys

input = sys.stdin.readline

def infect(hackedCom, n):
    global infomation
    INF = 10 ** 8
    minHeap = [(0, hackedCom)]
    infectionTime = [INF] * (n+1)
    infectionTime[hackedCom] = 0

    while minHeap:
        time, computer = h.heappop(minHeap)
        if time > infectionTime[computer]:
            continue

        for suspense, nextComputer in infomation[computer]:
            newTime = time + suspense
            if newTime < infectionTime[nextComputer]:
                infectionTime[nextComputer] = newTime
                h.heappush(minHeap,(newTime,nextComputer))

    cnt = 0
    maxTime = 0
    for t in infectionTime:
        if t != INF: # INF면 감염X 컴퓨터
            cnt += 1
            maxTime = max(maxTime, t)

    return [cnt, maxTime]

if __name__ == '__main__':
    trial = int(input())
    for _ in range(trial):
        infomation = defaultdict(list)
        # n : 컴퓨터 개수, d : 의존성 개수
        n, d, hackedCom = map(int,input().split(' '))
        for _ in range(d):
            a, b, s = map(int,input().split(' '))
            infomation[b].append((s, a))

        cnt, maxTime = infect(hackedCom, n)
        print(cnt, maxTime)