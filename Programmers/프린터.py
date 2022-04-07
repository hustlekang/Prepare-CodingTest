from collections import deque

def solution(priorities, location):
    arr = []
    for i in range(len(priorities)):
        arr.append((priorities[i], i))

    queue = deque(arr)
    cnt = 0
    while queue:
        priority, index = queue.popleft()
        otherPriority = [i[0] for i in queue]
        otherPriority.sort(reverse=True) # max()는 O(N),sort()는 O(NlogN)
        if otherPriority:
            if otherPriority[0] > priority:
                queue.append((priority, index))
            else:
                if index == location:
                    cnt += 1
                    break
                cnt += 1
        else:
            if index == location:
                cnt += 1
                break
            cnt += 1

    return cnt