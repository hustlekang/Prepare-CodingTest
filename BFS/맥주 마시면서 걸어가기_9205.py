from collections import deque
import sys
input = sys.stdin.readline

def caculateDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        startX, startY = map(int, input().split(' '))
        gs25 = set()
        visit = {}
        visit[(startX,startY)] = True

        for _ in range(n):
            x, y = map(int, input().split())
            gs25.add((x, y))
            visit[(x,y)] = False

        endX, endY = map(int, input().split(' '))
        visit[(endX, endY)] = False

        if caculateDistance(startX,startY,endX,endY) <= 1000:
            print('happy')
            continue

        queue = deque([(startX, startY)])
        answer = 'sad'

        while queue:
            x1, y1 = queue.popleft()

            if caculateDistance(x1,y1,endX,endY) <= 1000:
                answer = 'happy'
                break

            for x2, y2 in gs25:
                if not visit[(x2,y2)] and caculateDistance(x1,y1,x2,y2) <= 1000:
                    queue.append((x2, y2))
                    visit[(x2, y2)] = True

        print(answer)