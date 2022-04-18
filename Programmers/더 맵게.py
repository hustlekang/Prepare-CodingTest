import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            cnt = -1
            break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second * 2
        heapq.heappush(scoville, new)
        cnt += 1

    return cnt