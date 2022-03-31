n,m=map(int,input().split())
graph=[]
locationChicken=[]
locationHouse=[]
answer=100000
for i in range(n):
    line=list(map(int,input().split()))
    graph.append(line)
    for j in range(n):
        something=line[j]
        if something==2:
            locationChicken.append((i,j))
        elif something ==1:
            locationHouse.append((i,j))

cntChicken=len(locationChicken)
cntHouse=len(locationHouse)
distanceTable=[[0]*cntHouse for _ in range(cntChicken)]

for i in range(cntChicken):
    chicken = locationChicken[i]
    for j in range(cntHouse):
        house=locationHouse[j]
        distanceTable[i][j]=abs(chicken[0]-house[0])+abs(chicken[1]-house[1])

#조합 구하기
l = [x for x in range(cntChicken)]
N = len(l)
R = m
result = []

def combination(idx, list):
    if len(list) == R:
        result.append(list[:])
        return

    for i in range(idx, N):
        combination(i+1,list+[l[i]])

combination(0, [])

for select in result:
    new=[]
    distance=0
    for i in select:
        new.append(distanceTable[i])

    for j in range(cntHouse):
        distance+=min(k[j] for k in new)

    answer=min(answer,distance)

print(answer)