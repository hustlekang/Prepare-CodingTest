# 이진수가 0이 없으면 맨앞에 1을 0으로 바구고 그앞에 1을 붙혀줌
# Ex) 1111 -> 0111 -> 10111
# 0이 있으면 뒤부터 최초의 0을 1로 바꾸고 그 전의 1을 0으로 바꿔줌
# Ex) 1001 -> 1011 -> 1010
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(f(int(number)))
    return answer

def f(x):
    binNum=list(str(bin(x))[2:]) # bin()으로 2진수 변환시 앞에 붙는 '0b' 제거
    before=binNum
    binNum=list(binNum[::-1]) # 자리수 작은 뒤부터 봐야해서 for문 돌리기 편하게 배열 반전시킴

    for n in range(len(binNum)):
        if binNum[n]=='0':
            binNum[n]='1'
            if n-1>=0:
                binNum[n-1]='0'
            break

    binNum = binNum[::-1]
    if before==binNum: # 변한게 없으면 1로만 이루어진 것 ex) 11111
        binNum[0] = '0'
        binNum=['1']+binNum

    return int('0b'+"".join(binNum),2)