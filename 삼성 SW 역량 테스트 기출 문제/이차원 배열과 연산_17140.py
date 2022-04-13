from collections import Counter

r,c,k=map(int,input().split())
graph=[]
for _ in range(3):
    graph.append(list(map(int,input().split())))

sec=0
while True:
    if r-1<len(graph) and c-1<len(graph[0]): # 그래프 모양이 바뀌면서 [r-1,c-1]이 그래프를 벗어날 수도 있음
        if graph[r-1][c-1]==k:
            break

    sec+=1
    rowLength=len(graph)
    colLength=len(graph[0])
    if rowLength>= colLength: # R연산
        after=[]
        maxLength=0
        for line in graph:
            temp=[]
            numbers=list(set(line))
            if 0 in numbers: # 0은 카운팅x
                numbers.remove(0)
            numbers.sort()
            counter=Counter(line)
            for number in numbers:
                temp.append([number,counter[number]])
            temp.sort(key=lambda x:x[1])
            temp=sum(temp,[])
            maxLength=max(maxLength,len(temp))
            after.append(temp)

        for i in range(rowLength):
            if len(after[i])<maxLength:
                after[i]+=[0]*(maxLength-len(after[i]))

        graph=after

    else: # C연산
        after = []
        maxLength = 0
        for i in range(colLength):
            line=[row[i] for row in graph]
            temp=[]
            numbers=list(set(line))
            if 0 in numbers: # 0은 카운팅x
                numbers.remove(0)
            numbers.sort()
            counter = Counter(line)
            for number in numbers:
                temp.append([number,counter[number]])
            temp.sort(key=lambda x:x[1])
            temp=sum(temp,[])
            maxLength=max(maxLength,len(temp))
            after.append(temp)

        for i in range(colLength):
            if len(after[i]) < maxLength:
                after[i] += [0] * (maxLength - len(after[i]))

        changeRowCol=[] # 행,열 바꿔줘야함
        for i in range(len(after[0])):
            changeRowCol.append([col[i] for col in after])

        graph=changeRowCol

    if sec==101:
        sec=-1
        break

print(sec)