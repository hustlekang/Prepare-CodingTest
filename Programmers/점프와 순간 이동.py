# from collections import deque
# from sys import maxsize
# def solution(n):
#     visit = [maxsize] * (n + 1)
#     visit[1] = 1
#     queue = deque([1])
#     while queue:
#         number = queue.popleft()
#         if number*2 <= n: # visit 리스트의 크기보다 오버되면 안됨
#             if visit[number] < visit[int(number * 2)]:
#                 visit[int(number * 2)] = visit[number]
#                 queue.append(int(number * 2))
#         if number+1 <= n: # visit 리스트의 크기보다 오버되면 안됨
#             if visit[number] + 1 < visit[number + 1]:
#                 visit[number + 1] = visit[number] + 1
#                 queue.append(number + 1)
#
#     return visit[n]

# 결국 n이 짝수이면 f(n/2)와 동일하고
# 홀수이면 n-1이 짝수니 f((n-1)/2)의 값 + 1
def findRoot(n):
    if n==1:
        return 1
    if n%2==0:
        return findRoot(n//2)
    else:
        return findRoot((n-1)//2)+1

def solution(n):
    answer = findRoot(n)
    return answer