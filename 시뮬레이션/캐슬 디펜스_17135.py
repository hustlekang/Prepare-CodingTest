from itertools import combinations
from copy import deepcopy

def canAttackCoordinates(x, y, N, M, D):
    attackList = []
    center = (x, y)
    center_copy = center
    repeat = D - 1
    for _ in range(D):  # 궁수 위치 에서 위로 쭉
        nx = center[0] - 1
        center = (nx, center[1])
        attackList.append(center)

    for i in range(1, D):  # 궁수 위치 기준으로 왼쪽 부분 전부
        left = (center_copy[0], center_copy[1] - i)
        for _ in range(repeat):
            nx = left[0] - 1
            left = (nx, left[1])
            attackList.append(left)
        repeat -= 1

    repeat = D - 1  # 오른쪽도 봐야되니 repeat 초기화
    for i in range(1, D): # 궁수 위치 기준으로 오른쪽 부분 전부
        right = (center_copy[0], center_copy[1] + i)
        for _ in range(repeat):
            nx = right[0] - 1
            right = (nx, right[1])
            attackList.append(right)
        repeat -= 1

    return list(filter(lambda x: 0 <= x[0] < N and 0 <= x[1] < M, attackList)) # 그래프 정상 범위인 좌표만 리턴

def findClosest(x, y, arr): #x,y 와 가장 거리가 가까운 좌표값 배열에 담아 리턴
    distance = float('inf')
    list = []
    for point in arr:
        d = abs(x - point[0]) + abs(y - point[1])
        if d < distance:
            list = [point]
            distance = d
        elif d == distance:
            list.append(point)

    return list

N,M,D = map(int,input().split())
answer = float('-inf')
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))
graph.append([0]*M) # 궁수들 있는 곳

for combi in list(combinations([x for x in range(M)],3)): # 궁수 위치 완전 탐색
    graph_copy=deepcopy(graph) # 적들 전진시켜야되니 원본 배열 조작하면 안됨
    idx_1,idx_2,idx_3=combi
    archer1=(N,idx_1)
    archer2=(N,idx_2)
    archer3=(N,idx_3)
    kill=0
    for trial in range(N): # 맨 위에 있다 가정하고 최대 게임 횟수를 진행, 다 죽었나 확인 안함
        archer1_target= []
        archer2_target = []
        archer3_target = []
        all_target = []
        for point in canAttackCoordinates(archer1[0], archer1[1], N, M, D):# 좌표상 가능한 곳
            if graph_copy[point[0]][point[1]]==1: # 좌표상 가능한 곳 중에서 실제 적 있는 곳만
                archer1_target.append(point)
        for point in canAttackCoordinates(archer2[0], archer2[1], N, M, D):# 좌표상 가능한 곳
            if graph_copy[point[0]][point[1]]==1:
                archer2_target.append(point)
        for point in canAttackCoordinates(archer3[0], archer3[1], N, M, D):# 좌표상 가능한 곳
            if graph_copy[point[0]][point[1]]==1:
                archer3_target.append(point)

        targets = [
            findClosest(archer1[0], archer1[1], archer1_target),
            findClosest(archer2[0], archer2[1], archer2_target),
            findClosest(archer3[0], archer3[1], archer3_target)
        ]

        for target in targets:
            if len(target) == 0:
                continue
            elif len(target) == 1:
                all_target.append(target[0])
            else:
                all_target.append(sorted(target,key=lambda x:x[1])[0])

        for target in list(set(all_target)): # 궁수끼리 목표가 같을 수 있으니 set로 중복 제거후 사살
            graph_copy[target[0]][target[1]]=0
            kill+=1

        # 아래로 한칸씩 이동
        graph_copy.pop()
        graph_copy.pop()
        graph_copy.append([0]*M)
        graph_copy.insert(0,[0]*M)

    answer = max(answer,kill)

print(answer)