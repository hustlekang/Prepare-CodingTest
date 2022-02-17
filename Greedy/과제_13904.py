n=int(input())
graph=[[]for _ in range(1001)]
for _ in range(n):
    index,score=map(int,input().split())
    graph[index].append(score)

for i in range(1000,-1,-1):
    if len(graph[i])!=0:
        graph=graph[:i+1]
        break

for i in graph:
    i.sort(reverse=True)

score=0
partArr=[]
for i in range(len(graph)-1,0,-1):
    partArr+=graph[i]
    maximum=max(partArr)
    score+=maximum
    partArr[partArr.index(maximum)]=0

print(score)