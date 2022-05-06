from collections import deque
from copy import deepcopy

def solution(info, edges):
    answer = 0
    N=len(info) # 노드의 총 개수
    tree={i:[None,[]] for i in range(N)} # 노드번호:[ 동물종류,[ 자식노드들 ]]
    #tree 초기화
    for i in range(N):
        tree[i][0]=info[i]
    for edge in edges:
        parent,child=edge
        tree[parent][1].append(child)

    queue=deque([(0,0,0,[])]) # 노드번호,양수,늑대수,탐색할수있는 노드들

    while queue:
        node,sheep,wolf,nextNodes=queue.popleft()
        if tree[node][0]==0:
            sheep+=1
        else:
            wolf+=1

        if sheep>wolf: # 해당 노드를 방문하고 동물 수를 반영한 뒤 양이 늑대보다 많아야 더 진행이 가능
            answer=max(answer,sheep) # 답 초기화
            nextNodes+=tree[node][1] # 탐색할 수 있는 노드들에 자식 노드들 추가
            for nextNode in nextNodes: # 탐색할 수 있는 모든 노드들에 대해서 탐색을 진행
                copy_nextNodes = deepcopy(nextNodes)
                copy_nextNodes.remove(nextNode) # 자기 자신은 큐에 넣으면서 탐색하니까 제외하고
                queue.append((nextNode,sheep,wolf,copy_nextNodes))

    return answer