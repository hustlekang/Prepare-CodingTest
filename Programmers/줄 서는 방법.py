from math import ceil,factorial
# ex) arr=[1,2,3,4] 에서 15번째 수 구할 때
# 맨 앞 자리수 : arr에서 ceil(15/3!) 번째로 작은 수 = 3 , arr=[1,2,4]
# 두 번째 : arr에서 ceil(3/2!) 번째 수 = 2  , arr = [1,4]
# 세 번째 : arr에서 ceil(1/1!) 번째 수 = 1 , arr = [4]
# 네 번째 : arr에서 ceil(0/0!) 번째 수  = 4 , arr = []
def solution(n,k):
    answer=[]
    numbers=[i for i in range(1,n+1)]
    p=n-1

    while numbers:
        answer.append(numbers[ceil(k/factorial(p))-1])
        numbers.pop(ceil(k/factorial(p))-1)
        k %= factorial(p)
        p-=1

    return answer