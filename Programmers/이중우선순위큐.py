from collections import deque

def solution(operations):
    queue = deque([])
    for operation in operations:
        command, number = operation.split(' ')
        if command == 'I':
            queue.append(int(number))
            queue = deque(sorted(list(queue)))
        else:
            if len(queue) == 0:
                continue
            if number == '1':  # 최대값 제거
                queue.pop()
            else:  # 최솟값 제거
                queue.popleft()

    if queue:
        return [queue[-1], queue[0]]
    else:
        return [0, 0]