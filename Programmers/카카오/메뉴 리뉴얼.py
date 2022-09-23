from itertools import combinations
def solution(orders, course):
    answer = []
    people = {} # 사람번호 : {'A','B','C'..}
    totalPeople = len(orders)

    for i in range(totalPeople):
        people[i] = set(orders[i])

    for r in course:
        courseMenus = [] # r개로 만들 수 있는 코스
        maxCnt = 1 # 최소 2명으로부터 주문해야함

        possibleCourse = set()
        for order in orders:
            for combi in list(combinations(sorted(order), r)): # sorted해줘야 (x,y) (y,x) 같게 인식
                possibleCourse.add(combi)

        for foods in possibleCourse:
            cnt = 0 # 해당 음식 조합을 사람들이 시킨 횟수
            for idx, key in enumerate(people): # 모든 사람들에 대해 해당 조합 시킨 사람확인
                if totalPeople - idx < maxCnt - cnt: # 차이를 잡을 수 없으면 탐색 중지
                    break

                isOrdered = True
                for food in foods:
                    if food not in people[key]:
                        isOrdered = False
                        break

                if isOrdered: cnt += 1

            if maxCnt < cnt:
                maxCnt = cnt
                courseMenus = ["".join(sorted(list(foods)))]
            elif maxCnt == cnt and cnt > 1:
                courseMenus.append("".join(sorted(list(foods))))

        for courseMenu in courseMenus:
            answer.append(courseMenu)

    answer.sort()
    return answer


# 시간초과
# menu에 등장하는 모든 메뉴를 넣어두고 여기서 조합을 구하니까
# 애초에 불가능한 조합들도 탐색하게되면서 시간초과
# 사람1 : (a,b) 사람2: (f,c) 주문했을 때
# (a,f) 라는 조합은 아무도 주문 불가능하기 때문에 탐색할 필요가 없음
# -> 한 사람이 시킨 메뉴들에 대해서 조합으로 구해야함
from itertools import combinations

def solution(orders, course):
    answer = []
    people = {} # 사람번호 : {'A','B','C'..}
    totalPeople = len(orders)
    menu = set() # 모든 메뉴

    for i in range(totalPeople):
        people[i] = set(orders[i])
        menu = menu.union(set(orders[i]))

    for r in course:
        courseMenus = []
        maxCnt = 1 # 최소 2명으로부터 주문해야함

        for foods in list(combinations(menu,r)):
            cnt = 0 # 해당 음식 조합을 사람들이 시킨 횟수
            for idx, key in enumerate(people): # 모든 사람들에 대해 해당 조합 시킨 사람확인
                if totalPeople - idx < maxCnt - cnt: # 차이를 잡을 수 없으면 탐색 중지
                    break

                isOrdered = True
                for food in foods:
                    if food not in people[key]:
                        isOrdered = False
                        break

                if isOrdered: cnt += 1

            if maxCnt < cnt:
                maxCnt = cnt
                courseMenus = ["".join(sorted(list(foods)))]
            elif maxCnt == cnt and cnt > 1:
                courseMenus.append("".join(sorted(list(foods))))

        for courseMenu in courseMenus:
            answer.append(courseMenu)

    answer.sort()
    return answer


