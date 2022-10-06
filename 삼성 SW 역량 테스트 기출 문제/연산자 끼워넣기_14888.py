# Pypy3

def caculate(caculated, operatorIdx, numberIdx):
    result = 0
    if operators[operatorIdx] == '+':
        result = caculated + numbers[numberIdx]
    elif operators[operatorIdx] == '-':
        result = caculated - numbers[numberIdx]
    elif operators[operatorIdx] == '*':
        result = int(caculated * numbers[numberIdx])
    else:
        if caculated < 0:
            result = int(((caculated * (-1)) // numbers[numberIdx]) * -1)
        else:
            result = caculated // numbers[numberIdx]

    return result

def permutation(depth, caculated):
    if depth == N - 1:
        answer[0] = max(answer[0], caculated)
        answer[1] = min(answer[1], caculated)
        return

    for i in range(N-1):
        if not visit[i]:
            visit[i] = True
            permutation(depth + 1, caculate(caculated, i, depth + 1))
            visit[i] = False

if __name__ == '__main__':
    N = int(input())
    numbers = list(map(int, input().split(' ')))
    a, b, c, d = map(int, input().split(' '))
    operators  = []
    for _ in range(a): operators.append('+')
    for _ in range(b): operators.append('-')
    for _ in range(c): operators.append('*')
    for _ in range(d): operators.append('/')

    visit = [False] * (N - 1)
    answer = [(-1)*(10**10), 10**10] # 최대값, 최소값
    permutation(0, numbers[0])

    print("{}\n{}".format(answer[0], answer[1]))