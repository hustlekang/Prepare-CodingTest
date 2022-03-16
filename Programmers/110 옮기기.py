# 동일한 요소를 여러번 제거할 때, 스택 쓰면 log n 만에 제거 가능
def solution(s):
    answerList = []
    for x in s:
        cnt = 0
        stack = []
        for char in x:
            stack.append(char)
            if len(stack) >= 3:
                if stack[-3:] == ['1','1','0']:
                    for _ in range(3) : stack.pop()
                    cnt += 1

        idxOfZero=-1
        answer= None
        for i in range(len(stack)):
            if stack[i]=='0':
                idxOfZero=i

        if idxOfZero == -1: #0 이 없이 1111...이면 맨앞에 넣어줌
            answer = '110'*cnt + "".join(stack)

        else:
            answer = "".join(stack[:idxOfZero+1]) + '110'*cnt + "".join(stack[idxOfZero+1:])

        answerList.append(answer)

    return answerList