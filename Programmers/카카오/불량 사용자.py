# product([1,2],[a,b])    --> : (1,a),(1,b),(2,a),(2,b)
# product(*[[1,2],[a,b]]) --> : (1,a),(1,b),(2,a),(2,b)  인자가 2차원 배열이면 앞에 *
from itertools import product

def solution(user_id, banned_id):
    arr = []
    idIdx_table = []
    for i in range(len(banned_id)):
        idIdx_table.append((i, banned_id[i]))
    dic = [[] for _ in range(len(banned_id))]

    for idx in range(len(banned_id)):  # 벤아이디
        id = banned_id[idx]
        for user in user_id:  # 유저아이디
            isPossible = True
            if len(id) == len(user):
                for i in range(len(id)):
                    if id[i] == '*':
                        continue
                    if id[i] != user[i]:
                        isPossible = False
                        break

                if isPossible:
                    dic[idx].append(user)

    pick = list(product(*dic)) #한개씩 뽑은 조합들
    for each in pick:
        if len(each) == len(set(each)): #유저 한명이 여러 벤 아이디에 해당할 순 없다, set화시켰을 때 달라지면 중복된거
            arr.append(list(each))

    for i in arr:
        i.sort() #선택한 조합들끼리 정렬을해서 맞춰준다

    for i in range(len(arr)):
        arr[i] = "".join(arr[i]) # 배열이기때문에 set화시키기위해 문자열로 합쳐준다

    answer = len(list(set(arr))) # 다른 banned_id에 해당되는 사용자여도 결국 정지당한 사용자들의 조합이므로 중복 제거

    return answer