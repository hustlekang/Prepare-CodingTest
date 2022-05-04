def caculate(list): #[숫자,'연산자',숫자] 를 계산 [[],'연산자',[]] 꼴이면 재귀로 해결
    isOk = True
    for each in list:
        if type(each) == type([]):
            isOk = False
            break

    if isOk: # 재귀 탈출 조건
        if list[1] == '-':
            return list[0] - list[2]
        elif list[1] == '*':
            return int(list[0] * list[2])
        else:
            return list[0] + list[2]

    if list[1] == '-':
        if type(list[0]) == type([]) and type(list[2]) == type([]):
            return caculate(list[0]) - caculate(list[2])
        elif type(list[0]) == type([]):
            return caculate(list[0]) - list[2]
        elif type(list[2]) == type([]):
            return list[0] - caculate(list[2])

    elif list[1] == '*':
        if type(list[0]) == type([]) and type(list[2]) == type([]):
            return int(caculate(list[0]) * caculate(list[2]))
        elif type(list[0]) == type([]):
            return int(caculate(list[0]) * list[2])
        elif type(list[2]) == type([]):
            return int(list[0] * caculate(list[2]))

    else:
        if type(list[0]) == type([]) and type(list[2]) == type([]):
            return caculate(list[0]) + caculate(list[2])
        elif type(list[0]) == type([]):
            return caculate(list[0]) + list[2]
        elif type(list[2]) == type([]):
            return list[0] + caculate(list[2])

def solution(expression):
    answer=0
    priority = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '-', '+'],
        ['*', '+', '-']
    ]
    arr=[] # '100*200-30'을  [100,'*',200,'-',30] 꼴로 만든다
    temp = ''

    for each in expression:
        if each.isdigit():
            temp += each
        else:
            arr.append(int(temp))
            arr.append(each)
            temp = ''
    arr.append(int(temp))

    for sequence in priority:
        trialArr=arr
        for operator in sequence: # [x,'연산자',y] 꼴로 만든다, 우선 순위를 (x*y) 묶어주는 것 처럼
            while operator in trialArr:
                idx=trialArr.index(operator)
                trialArr=trialArr[:idx-1]+[trialArr[idx-1:idx+2]]+trialArr[idx+2:]

        answer=max(answer,abs(caculate(trialArr[0]))) # trialArr=[[x,'연산자',y]] 꼴이므로 trialArr[0]을 caculate()에 인수로

    return answer