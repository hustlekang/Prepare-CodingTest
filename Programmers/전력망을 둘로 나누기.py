from collections import deque
def solution(n, wires):
    answer=n # 차이는 n보다 무조건 작기 때문에 n으로 설정후 구한 값이 n보다 작을 때마다 갱신
    # 모든 연결 요소를 차례대로 1개를 끊어 버리고 1번 노드와 연결된 노드가 몇개인지 계산
    # wires[]의 앞에서 부터 뺏다가 계산 끝나고 맨뒤로 넣어서 wires[] 유지하는 방식 pop(0) -> append(pop(0))
    for _ in range(n - 1):
        cutted = wires.pop(0)
        visit=[False]*(n+1)
        graph = [[] for _ in range(n + 1)]

        for connect in wires:
            nodeA, nodeB = connect
            graph[nodeA].append(nodeB)
            graph[nodeB].append(nodeA)

        visit[1]=True
        queue=deque([1]) #1번 노드를 넣어서 연결 노드 개수 BFS로 파악
        cnt=1 # 연결된 노드 수

        while(queue):
            node=queue.popleft()
            for nextNode in graph[node]:
                if not visit[nextNode]:
                    cnt+=1
                    queue.append((nextNode))
                    visit[nextNode]=True

        connect1=cnt
        connect2=n-cnt
        answer=min(answer,abs(connect2-connect1))

        # answer 구하고 제거 했던 연결 요소 다시 넣어줌
        wires.append(cutted)

    return answer