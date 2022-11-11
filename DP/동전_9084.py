import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        coins = list(map(int, input().split()))
        target = int(input())
        dp = [0] * (target + 1) # dp[금액] = 방법의 수
        dp[0] = 1

        for coin in coins:
            for money in range(coin, target + 1):
                dp[money] += dp[money - coin]

        print(dp[target])