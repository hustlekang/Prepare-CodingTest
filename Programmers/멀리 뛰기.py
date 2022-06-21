def solution(n):
    answerList=[-1]*2001
    answerList[1]=1
    answerList[2]=2
    for i in range(3,2000):
        answerList[i]=answerList[i-1]+answerList[i-2]
    answer=answerList[n] % 1234567
    return answer

# 1 과 2의 갯수를 구하고 같은 것이 있는 순열 방식 : 시간 초과
# from math import factorial
# def solution(n):
#     answer=0
#     cnt_of_2=n//2
#     for i in range(cnt_of_2+1):
#         two=i
#         one=n-(2*i)
#         answer+=int(factorial(one+two)/(factorial(one)*factorial(two)))
#
#     return answer%1234567

# 수직선 BFS 방식 : 시간초과
# from collections import deque
# def solution(n):
#     cnt=0
#     queue=deque([0])
#     while queue:
#         number=queue.popleft()
#         if number==n:
#             cnt+=1
#             continue
#         if number+1 <= n:
#             queue.append(number+1)
#         if number+2 <=n:
#             queue.append(number+2)
#
#     return cnt%1234567