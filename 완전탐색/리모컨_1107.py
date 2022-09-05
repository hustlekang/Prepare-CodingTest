def solution():
    target = input().strip()
    if target == '100':
        return 0

    answer = abs(int(target) - 100) # +,-로 100에서 부터 조작한 횟수
    uselessCnt = int(input())
    useless = set()
    if uselessCnt != 0:
        useless = set(input().strip().split(' '))

    for n in range(10 ** 6 + 1):  # n은 0 ~ 100만까지 모든 숫자
        for eachNum in str(n):  # n의 각각 자리수에 대해
            if eachNum in useless: # 만들 수 없는 숫자면
                break
        else:  # break가 발생하지 않았을 때 = 만들 수 있는 숫자일 때
            cnt = len(str(n)) + abs(int(target) - n) # 숫자 누르는 횟수 + (+,- 조작 횟수)
            answer = min(answer, cnt)

    return answer

print(solution())