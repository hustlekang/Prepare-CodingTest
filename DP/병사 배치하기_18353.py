import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int,input().split(' ')))
    dp = [0] * N # numbers[i]를 마지막으로 배치할 때 최대 병사 수
    dp[0] = 1 # 첫번째는 그냥 1명 배치

    for i in range(1, N):
        maxValue = 0
        for j in range(i): # 이전의 값들을 전부 탐색
            if numbers[j] > numbers[i]: # 이전 숫자가 더 크면 가능한 배치
                maxValue = max(maxValue, dp[j])
        dp[i] = 1 + maxValue

    answer = N - max(dp)
    print(answer)