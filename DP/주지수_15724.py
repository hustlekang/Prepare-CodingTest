import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    dp = [list(map(int, input().split())) for _ in range(N)]

    # 가로로 누적합
    for i in range(N):
        for j in range(1, M):
            dp[i][j] += dp[i][j-1]
    # 세로로 누적합
    for j in range(M):
        for i in range(1, N):
            dp[i][j] += dp[i-1][j]

    for _ in range(int(input())):
        x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())

        if 0 < x1 and 0 < y1:
            answer = dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1]) + dp[x1-1][y1-1]
        elif 0 < x1:
            answer = dp[x2][y2] - dp[x1-1][y2]
        elif 0 < y1:
            answer = dp[x2][y2] - dp[x2][y1-1]
        else:
            answer = dp[x2][y2]

        print(answer)