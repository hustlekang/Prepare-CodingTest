import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    graph = [list(map(int, input().strip().split(' '))) for _ in range(n)]
    dp = [[0] * i for i in range(1, n+1)]
    dp[0][0] = graph[0][0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0: # 맨 왼쪽은 바로 위에서 오는 값밖에 못받음
                dp[i][j] = dp[i-1][0] + graph[i][j]
            elif j == i: # 맨 오른쪽도 바로 위에서 오는 값밖에 못받음
                dp[i][j] = dp[i-1][-1] + graph[i][j]
            else: # 왼쪽 위, 오른쪽 위 2개중 큰 값을 받으면 최대값
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + graph[i][j]

    answer = max(dp[-1])
    print(answer)