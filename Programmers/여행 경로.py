from collections import defaultdict
answer = []
dic = defaultdict(list)

def dfs(start):
    while dic[start]:
        dfs(dic[start].pop())

    if len(dic[start])==0:
        answer.append(start)
        return

def solution(tickets):
    global answer
    for ticket in tickets:
        dic[ticket[0]].append(ticket[1])

    for key in dic.keys():
        dic[key].sort(reverse=True)

    dfs('ICN')
    answer = answer[::-1]
    return answer