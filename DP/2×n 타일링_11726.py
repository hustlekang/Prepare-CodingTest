dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3,1001):
    dp[i] = dp[i-1] + dp[i-2]

if __name__ == '__main__':
    n = int(input())
    print(dp[n] % 10007)

# 오버플로인가
factorial = [1] * 1001
for i in range(2,1001):
    factorial[i] = (factorial[i-1] * i)

if __name__ == '__main__':
    n = int(input())
    answer = 1 # 모두 세로로 배치하는 경우

    # a : 가로의 개수, b : 세로의 개수
    for a in [i for i in range(1, n//2 + 1)]:
        b = n - int(2 * a)
        cnt = factorial[a+b] / (factorial[a] * factorial[b])
        answer += int(cnt)
        answer %= 10007

    print(answer)