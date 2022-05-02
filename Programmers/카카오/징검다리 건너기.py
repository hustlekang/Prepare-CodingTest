def solution(stones, k):
    answer = 0
    left = 0
    right = 10 ** 9
    while left <= right:
        mid = (left + right) // 2  # 이미 지나간 사람 수
        jump = 0
        isPossible = True

        for i in range(len(stones)):
            if jump == k: # 계속 0이어서 jump가 증가되면 안되는 건데 시간 낭비
                isPossible = False
                break

            if stones[i] - mid > 0:  # 디딤돌이 0 보다 클 때
                if jump + 1 <= k:
                    jump = 0 # 새로운 디딤돌까지 이동이 가능하니 jump=0 초기화
                else: # 이동 불가 탐색 종료
                    isPossible = False
                    break

            else:  # 디딤돌이 0 일때
                jump += 1

        else:  # for문을 break로 탈출하지 않았다면 마지막 디딤돌에 서 있는 상황, 한 발자국 더 가야함
            if jump + 1 > k:
                isPossible = False

        if isPossible:  # 가능하니까 사람수를 더 늘려보자
            left = mid + 1
            answer = max(answer, mid + 1)

        else:
            right = mid - 1

    return answer