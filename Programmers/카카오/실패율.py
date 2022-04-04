def solution(N, stages):
    information = [[0, 0] for _ in range(N + 2)]  # [아직못깬애,도달한사람]
    newArr = []
    for i in stages:
        information[i][0] += 1  # 아직못깬애
        for j in range(1, i + 1):
            information[j][1] += 1 #도달한사람

    for i in range(1, len(information) - 1):
        if information[i][1] == 0:
            newArr.append((i, 0))
        else:
            newArr.append((i, information[i][0] / information[i][1]))

    newArr.sort(key=lambda x: x[0])
    newArr.sort(key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in newArr]

    return answer