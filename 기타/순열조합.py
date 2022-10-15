def product(arrs):
    result = [[]]
    for arr in arrs:
        result = [x+[y] for x in result for y in arr]
    return result


def permutation(depth, tempArr):
    if depth == r:
        result.append(tempArr[:])
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            permutation(depth + 1, tempArr + [arr[i]])
            visit[i] = False


def combination(depth, startIdx, tempArr):
    if depth == r:
        result.append(tempArr[:])

    for i in range(startIdx, n):
        combination(depth+1, i+1, tempArr + [arr[i]])


if __name__ == '__main__':
    arr = [1,2,3,4]
    n = len(arr)
    r = 2
    visit = [False] * n
    result = []

    combination(0,0,[])
    print(result)
    result.clear()
    permutation(0,[])
    print(result)
    print(product([[1,2,3],[10,20,30],[100,200,300]]))
