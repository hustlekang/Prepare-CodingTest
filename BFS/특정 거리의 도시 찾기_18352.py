from collections import deque
import sys

N,M,K,X=map(int,sys.stdin.readline().split())
answers=[]
connection=[[] for _ in range(N+1)]
visit=[False]*(N+1)

for _ in range(M):
    start,end=map(int,sys.stdin.readline().split())
    connection[start].append(end)

queue = deque([(X,0)])
visit[X]=True
while queue:
    node,distance=queue.popleft()
    if distance==K:
        answers.append(node)
        continue

    if distance<K:
        for next in connection[node]:
            if visit[next]==False:
                visit[next]=True
                queue.append((next,distance+1))

if len(answers)==0:
    print(-1)
else:
    answers.sort()
    for answer in answers:
        print(answer)