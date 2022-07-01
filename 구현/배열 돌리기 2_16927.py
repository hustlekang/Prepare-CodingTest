from collections import deque
from copy import deepcopy

N,M,R=map(int,input().split())
visit=[[False]*M for _ in range(N)]
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(min(N,M)): # 왼쪽 상단 모서리 기준으로 회전시킬꺼 (0,0)->(1,1)
    if visit[i][i]: #
        break

    left = [x[i] for x in graph]
    right = [x[M-(i+1)] for x in graph]
    top = deepcopy(graph[i]) # pop 해야되기 때문에 깊은 복사 안하면 graph 바뀜
    bottom = deepcopy(graph[N - (i + 1)])

    for _ in range(i):
        left.pop(0)
        left.pop()
        right.pop(0)
        right.pop()
        top.pop(0)
        top.pop()
        bottom.pop(0)
        bottom.pop()

    right.reverse()
    top.reverse()

    # 연결을 위해 모서리 중복 되는 부분 제거
    left.pop()
    bottom.pop()
    right.pop()
    top.pop()

    rotateCnt = R % (2 * (N-(2*i) + M-(2*i)) - 4) # 네변의 길이 - 4 가 사이클임
    queue = deque(left+bottom+right+top)
    queue.rotate(rotateCnt)
    queue = list(queue) # 슬라이싱을 위해 리스트로 변환

    new_left = queue[:N-(2*i)]
    new_bottom = queue[N-(2*i)-1:N-(2*i)-1+(M-(2*i))]
    new_right = queue[N-(2*i)-1+(M-(2*i))-1:N-(2*i)-1+(M-(2*i))-1+(N-(2*i))]
    new_top = queue[N-(2*i)-1+(M-(2*i))-1+(N-(2*i))-1:]+[queue[0]]

    new_right.reverse()
    new_top.reverse()

    for j,item in zip(range(i,i+N-(2*i)+1),new_left):
        graph[j][i]=item
        visit[j][i]=True

    for j,item in zip(range(i,i+M-(2*i)+1),new_bottom):
        graph[N-(i+1)][j] = item
        visit[N - (i + 1)][j]=True

    for j,item in zip(range(i,i+N-(2*i)+1),new_right):
        graph[j][M-(i+1)]=item
        visit[j][M-(i+1)]=True

    for j,item in zip(range(i,i+M-(2*i)+1),new_top):
        graph[i][j] = item
        visit[i][j]=True

for line in graph:
    print(" ".join(map(str,line)))