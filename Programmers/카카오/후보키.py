# setA.issubset(setB) setA가 setB의 부분집합이면 True

from itertools import combinations

def solution(relation):
    answer = 0
    table = []
    col_len = len(relation)
    attribute_len = len(relation[0])
    willdel=[]

    for i in range(attribute_len): ##가로 세로 바꿔줌 계산 편하게
        table.append([arr[i] for arr in relation])

    for i in table: # 속성 하나로 후보키 되는 애들 카운트
        if sorted(list(set(i))) == sorted(i):
            answer += 1
            willdel.append(i)

    for i in willdel: #1개로 되는 속성들 제거
        table.remove(i)

    n = len(table)
    r = 2
    already = []
    while n>=r: #nCr 이므로
        select = list(combinations([x for x in range(n)], r)) #후보키 조합 선정
        for combi in select:
            new = []
            for col in range(col_len):
                temp = ''
                for i in combi:
                    temp+= table[i][col]
                new.append(temp)

            if sorted(list(set(new))) == sorted(new):
                isLeast=True
                for item in already:
                    if item.issubset(set(combi)): #유일성 체크
                        isLeast=False
                        break

                if isLeast:
                    already.append(set(combi))
                    answer += 1
        r += 1

    return answer
