from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
INF = 10 ** 8

if __name__ == '__main__':
    N, K = map(int, input().split(' '))
    sec = [INF] * 100001
    sec[N] = 0
    minHeap = [(0, N)]

    while minHeap:
        s, location = heappop(minHeap)

        if location == K:
            break
        if s > sec[location]:
            continue

        for nextLocation, cost in zip([int(location * 2), location - 1, location + 1],[0, 1, 1]):
            newS = s + cost
            if 0 <= nextLocation <= 100000 and newS < sec[nextLocation]:
                sec[nextLocation] = newS
                heappush(minHeap, (newS, nextLocation))

    answer = sec[K]
    print(answer)