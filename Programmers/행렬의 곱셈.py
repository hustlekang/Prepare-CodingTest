def solution(arr1, arr2):
    arr2_vertical = []
    for i in range(len(arr2[0])):
        arr2_vertical.append([line[i] for line in arr2])

    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2_vertical)):
            calculated = 0
            for n1, n2 in zip(arr1[i], arr2_vertical[j]):
                calculated += n1 * n2
            answer[i][j] = calculated

    return answer