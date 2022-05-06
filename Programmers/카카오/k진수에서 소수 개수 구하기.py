# 가장 큰 수인 100만을 이진수로 바꾸면 11110100001001000000인데
# 이 수는 sys.maxsize보다 크기 때문에 isPrime[] 배열을 숫자만큼 만들 수 없음
# 숫자별로 소수인지 파악해야함
# 2~자기자신-1 까지 체크하면 시간초과나니까
# 2~sqrt(자기자신) 까지 나눠지는지 체크
from math import sqrt

def trans(n,k):
    if k==10:
        return str(n)
    string='0123456789'
    answer=''
    while n>0:
        answer+=string[n % k]
        n//=k
    return answer[::-1]

def solution(n, k):
    answer=0
    arr=trans(n,k).split('0')
    for number in arr:
        if number=='' or number=='1':
            continue

        isPrime=True
        for p in range(2,int(sqrt(int(number)))+1):
            if int(number)%p==0:
                isPrime=False
                break
        if isPrime:
            answer+=1

    return answer