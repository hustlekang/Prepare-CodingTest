from collections import deque
INF = 10 ** 8

if __name__ == '__main__':
    N, K = map(int, input().split(' '))
    time = [INF] * 100010
    beforeNodeInfo = [-1] * 100010
    answer = INF
    ways = [K]
    queue = deque([(0, N)])

    while queue:
        sec, subin = queue.popleft()
        if subin == K:
            if sec < answer:
                answer = sec
            break

        if subin * 2 <= 100009 and sec + 1 < time[int(subin * 2)]:
            time[int(subin * 2)] = sec + 1
            queue.append((sec+1, int(subin*2)))
            beforeNodeInfo[int(subin * 2)] = subin

        if subin + 1 <= 100009 and sec + 1 < time[subin + 1]:
            time[subin + 1] = sec + 1
            queue.append((sec+1,subin+1))
            beforeNodeInfo[subin+1] = subin

        if 0 <= subin - 1 <= 100009 and sec + 1 < time[subin - 1]:
            time[subin - 1] = sec - 1
            queue.append((sec+1,subin-1))
            beforeNodeInfo[subin-1] = subin

    start = K
    for _ in range(answer):
        ways.append(beforeNodeInfo[start])
        start = beforeNodeInfo[start]

    print(answer)
    print(*ways[::-1])