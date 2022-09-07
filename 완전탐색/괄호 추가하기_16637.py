from itertools import combinations

def caculate(a, operator, b):
    if operator == '*':
        return int(a) * int(b)
    elif operator == '+':
        return int(a) + int(b)
    else:
        return int(a) - int(b)

def solution(equation, priority): # equation = 문자열 수식, priority = [괄호로 묶인 연산자의 인덱스,...]
    priority = set(priority) # in 연산 O(1) 위해서 set로
    result = int(equation[0]) # 수식의 첫 숫자를 result로 초기화
    i = 1 # 수식에서 계산할 연산자의 인덱스

    while i < len(equation): # 수식의 길이보다 커지면 더이상 계산할 연산자 존재 X
        if i + 2 < len(equation) and i + 2 in priority: # 지금 계산하려는 연산자 다음 연산자가 괄호로 묶여있으면
            braketResult = caculate(equation[i + 1], equation[i + 2], equation[i + 3]) # 괄호를 먼저 계산
            result = caculate(result, equation[i], braketResult) # 기존답과 괄호 계산 결과를 연산
            i += 4 # 현재 연산자 다음 괄호연산자까지 계산이 됐기에 다음 다음
        else: # 현재 계산하려는 연산자 다음이 괄호로 묶이지 않으면
            result = caculate(result, equation[i], equation[i + 1])
            i += 2 # 다음 연산자로 이동, 연산자 사이에 숫자 있어서 +2임

    return result

if __name__ == '__main__':
    N = int(input())
    equation = input().strip()
    operator_idx = [2*x+1 for x in range(int((N-1)/2))] # 수식에서 연산자의 인덱스들이 든 리스트
    length = len(operator_idx)
    answer = -2**31 # 최소값 설정

    # 전체 연산자 중에서 괄호로 묶을 연산자는 절반까지만 보면됨
    # 괄호 겹치므로 4칸이상 띄워져야함, 3+8*7 에서 +와 *는 동시에 괄호로 묶을 수 없음
    # (3+(8)*7) 불가능
    for r in range(length//2 +1):
        for combi in list(combinations(operator_idx,r)):
            pick = list(combi)
            possible = True
            for i in range(len(pick)-1):
                if pick[i+1] - pick[i] < 4:
                    possible = False
                    break

            if possible:
                answer = max(answer, solution(equation,pick))

    print(answer)