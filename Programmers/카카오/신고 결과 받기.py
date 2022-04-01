def solution(id_list, report, k):
    userIdx = {}
    idx = 0
    for id in id_list:
        userIdx[id] = idx
        idx += 1

    n = len(id_list)
    cnt = [0] * n
    willGetMail = [[] for _ in range(n)]
    answer = [0] * n

    for i in report:
        er, ed = i.split(' ')
        if er in willGetMail[userIdx[ed]]:
            continue
        cnt[userIdx[ed]] += 1
        willGetMail[userIdx[ed]].append(er)

    for i in range(n):
        if cnt[i] >= k:
            for personWillgetMail in willGetMail[i]:
                answer[userIdx[personWillgetMail]] += 1

    return answer