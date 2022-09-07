def solution(alp, cop, problems):
    INF = 10**8
    target_alp = 0 # 목표 알고력
    target_cop = 0 # 목표 코딩력

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems: # 최대값으로 목표 설정
        target_alp = max(target_alp, alp_req, alp) # 목표가 현재보다 낮으면 -> dp[현재][현재]가 존재하지 않아서 에러
        target_cop = max(target_cop, cop_req, cop)


    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)] # dp[x][y] = 알고력:x, 코딩력:y를 충족한 최소 시간
    dp[alp][cop] = 0 # 초기 알고력,코딩력을 만족시키는 시간은 0

    maxX = target_alp + 1
    maxY = target_cop + 1

    # 현재 알고력,코딩력부터 목표까지 dp 갱신
    for x in range(alp,target_alp + 1):
        for y in range(cop, target_cop + 1):
            if x + 1 < maxX: # dp 범위 벗어나지 않을 때
                dp[x+1][y] = min(dp[x+1][y], dp[x][y] + 1) # 알고리즘 공부
            if y + 1 < maxY: # dp 범위 벗어나지 않을 때
                dp[x][y+1] = min(dp[x][y+1], dp[x][y] + 1) # 코딩테스트 공부

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if x >= alp_req and y >= cop_req: # 풀 수 있는 문제일 때
                    if x + alp_rwd >= maxX and y + cop_rwd >= maxY: # dp[][] 범위를 x,y 모두 넘어갈 때
                        dp[maxX-1][maxY-1] = min(dp[maxX-1][maxY-1], dp[x][y] + cost)
                    elif x + alp_rwd >= maxX: # dp[][] 범위를 x가 넘어갈 때
                        dp[maxX-1][y+cop_rwd] = min(dp[maxX-1][y+cop_rwd], dp[x][y] + cost)
                    elif y + cop_rwd >= maxY: # dp[][] 범위를 y가 넘어갈 때
                        dp[x+alp_rwd][maxY-1] = min(dp[x+alp_rwd][maxY-1], dp[x][y] + cost)
                    else: # dp[][] 범위 안에 있을 때
                        dp[x+alp_rwd][y+cop_rwd] = min(dp[x+alp_rwd][y+cop_rwd], dp[x][y] + cost)

    answer = dp[target_alp][target_cop]
    return answer