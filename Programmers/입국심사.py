# def solution(n, times):
#     left = 0
#     right = 10 ** 18
#     answer = 10 ** 18
#     while left <= right:
#         mid = (left + right) // 2
#         howManyPeople = 0
#         for time in times:
#             howManyPeople += mid // time
#             if howManyPeople >= n:
#                 break
#         if howManyPeople < n:
#             left = mid + 1 # +1 까먹지말자
#         else:
#             answer = min(answer, mid)
#             right = mid - 1 # -1 까먹지말자
#
#     return answer
import math
n=int(input())
answer=0
for i in range(1,n+1):
    sum=0
    for j in range(1,int(math.sqrt(i))+1):
        if i%j==0:
            sum+=j
            sum+=i//j
    answer+=sum
print(answer)