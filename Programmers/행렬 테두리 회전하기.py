def solution(rows, columns, queries):
    graph = []
    start = 1
    end = columns
    answer = []
    for _ in range(rows):
        temp = [x for x in range(start, end + 1)]
        start += columns
        end += columns
        graph.append(temp)

    for movingIdx in range(len(queries)):
        graph, minimum = rotate(graph, queries[movingIdx])
        answer.append(minimum)

    return answer

def rotate(graph,moving):
    x1,y1,x2,y2=moving[0]-1,moving[1]-1,moving[2]-1,moving[3]-1
    temp=graph[x1][y1]
    minimum=temp
    #맨위 왼쪽을 temp에 담아두고 그 오른쪽부터 회전된 값을 채워나감, 시계방향으로
    #  ^ 시작--->
    #  |       |
    #  |       |
    #  <-------V
    for y in range(y1+1,y2+1):
        now=graph[x1][y]
        graph[x1][y]=temp
        temp=now
        if temp<minimum:
            minimum=temp
    for x in range(x1+1,x2+1):
        now=graph[x][y2]
        graph[x][y2]=temp
        temp=now
        if temp<minimum:
            minimum=temp
    for y in range(y2-1,y1-1,-1):
        now=graph[x2][y]
        graph[x2][y]=temp
        temp=now
        if temp<minimum:
            minimum=temp
    for x in range(x2-1,x1-1,-1):
        now=graph[x][y1]
        graph[x][y1]=temp
        temp=now
        if temp<minimum:
            minimum=temp

    return [graph,minimum]