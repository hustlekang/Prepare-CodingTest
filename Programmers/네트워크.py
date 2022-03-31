from collections import deque
def solution(n, computers):
    answer = 0
    visit = [False] * n
    queue = deque([])
    for startNode in range(n):
        if not visit[startNode]:
            queue.append(startNode)
            visit[startNode] = True
            while queue:
                node = queue.popleft()
                for i in range(len(computers)):
                    if computers[node][i] == 1 and not visit[i]:
                        visit[i] = True
                        queue.append(i)
            answer += 1

    return answer