import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(node, cnt):
    global answer, visit
    visit[node] = True
    if cnt == 5 or answer == 1: # 연결이 5개면 종료
        answer = 1
        return
    
    for nextNode in connection[node]:
        if not visit[nextNode]:
            dfs(nextNode,cnt + 1)
            visit[nextNode] = False # for문 다음으로 넘어가기 전에 방문 했던건 초기화 해야함

if __name__ == '__main__':
    answer = 0
    N, M = map(int, input().split(' '))
    connection = [[] for _ in range(N)]
    visit = [False] * N
    for _ in range(M):
        a, b = map(int, input().split(' '))
        connection[a].append(b)
        connection[b].append(a)

    for node in range(N):
        dfs(node,1)
        visit = [False] * N

    print(answer)