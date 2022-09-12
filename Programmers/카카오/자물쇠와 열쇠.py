def rotate(graph): # 2차원 배열 오른쪽으로 90도 회전하는 함수
    l = len(graph)
    rotated = [[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            rotated[i][j] = graph[l-j-1][i]

    return rotated

def solution(key, lock):
    N = len(lock)
    M = len(key)
    K = N + 2*(M-1) # lock을 정중앙에 배치하고 key와 1개 겹쳐 있는 최대 크기의 길이
    graph = [[0]*K for _ in range(K)]

    def check(): # graph에서 lock의 위치만 돌기와 홈이 다 맞았는지 체크하는 함수
        for x in range(M-1,M-1+N):
            for y in range(M-1,M-1+N):
                if graph[x][y] != 1:
                    return False
        return True

    # 정 중앙에 lock을 배치
    for x in range(N):
        for y in range(N):
            graph[x+(M-1)][y+(M-1)] = lock[x][y]

    # lock에 홈이 없어서 key가 필요 없을 때
    if check():
        return True

    for x in range(K-(M-1)): # K-(M-1) 부터는 lock이 있는 부분을 넘어가기 때문에 볼 필요 X
        for y in range(K-(M-1)):
            for _ in range(4): # 회전한 다음 체크
                key = rotate(key)
                for i in range(M): # 회전한 key의 모든 값들을 graph에 넣어줌
                    for j in range(M):
                        graph[i+x][j+y] += key[i][j]

                if check():
                    return True

                for i in range(M): # graph에서 다시 빼서 원래 상태로 되돌림
                    for j in range(M):
                        graph[i+x][j+y] -= key[i][j]

    return False