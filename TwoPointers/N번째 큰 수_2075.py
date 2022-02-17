#pypy3 일때 정답, python3은 시간초과
import heapq,sys
n=int(input())
graph=[]
answer=None
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

start= [n-1,graph[n-1].index(max(graph[n-1]))]
heap=[]
cnt=0
heapq.heappush(heap,(graph[start[0]][start[1]]*-1 , start))
graph[start[0]][start[1]]=-1000000001

while(cnt<n):
    v,coordinate=heapq.heappop(heap)
    v *=-1
    cnt+=1
    if cnt==n:
        answer=v
        break

    heapq.heappush(heap,(graph[coordinate[0]-1][coordinate[1]]*-1 ,[coordinate[0]-1,coordinate[1]]))
    graph[coordinate[0] - 1][coordinate[1]]=-1000000001
    rx,ry=coordinate[0], graph[coordinate[0]].index(max(graph[coordinate[0]]))
    heapq.heappush(heap,(graph[rx][ry]*-1,[rx,ry]))
    graph[rx][ry]=-1000000001

print(answer)