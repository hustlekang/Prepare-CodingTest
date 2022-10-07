import sys
input = sys.stdin.readline
INF = 10 ** 5

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    connection = [[INF] * n for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split(' '))
        if c < connection[a - 1][b - 1]:
            connection[a - 1][b - 1] = c

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if start==end:
                    connection[start][end] = 0
                    continue

                newWay = connection[start][mid] + connection[mid][end]
                if newWay < connection[start][end]:
                    connection[start][end] = newWay

    for i in range(n):
        for j in range(n):
            if connection[i][j] == INF:
                connection[i][j] = 0

    for line in connection:
        print(*line)