def solution(x, y, n):
    INF = 10_000_000
    dp = [INF] * 1_000_001
    dp[x] = 0

    for i in range(x, y + 1):
        a = i - n
        b = int(i / 3) if i % 3 == 0 else -1
        c = int(i / 2) if i % 2 == 0 else -1

        indexes = [a, b, c]

        for j in indexes:
            if j % 1 == 0 and x <= j and dp[j] != INF:
                dp[i] = min(dp[i], dp[j] + 1)

    answer = dp[y] if dp[y] != INF else -1

    return answer