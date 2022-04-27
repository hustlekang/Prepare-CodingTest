def solution(enroll, referral, seller, amount):
    profit = {'-': 0}  # 사람당 판매금액
    parents = {'-': 'root'}
    answer = []

    for person in enroll: # 사람당 판매금액 초기화
        profit[person] = 0

    for i in range(len(enroll)): # 부모 노드 세팅
        parents[enroll[i]] = referral[i]

    for i in range(len(seller)):
        person = seller[i]
        money = int(amount[i] * 100)

        while parents[person] != 'root':
            parent = parents[person]  # 부모 노드 설정
            if (money * 0.1) >= 1:
                profit[person] += money - int(money * 0.1)  # 자기 몫 90%
                money = int(money * 0.1)
                person = parent
                if person == '-': # root 노드일때
                    profit[person] += money
            else:
                profit[person] += money # 10%가 1원 미만이면 꿀꺽
                break

    for person in enroll:
        answer.append(profit[person])

    return answer