# Pypy3

def combination(depth, startIdx, tempSet):
    if depth == R:
        combinations.append(tempSet.copy())
        return

    for i in range(startIdx, N):
        combination(depth + 1, i + 1, tempSet.union({i}))

def getScore(teamSet):
    score = 0
    n = len(teamSet)
    team = list(teamSet)

    for i in range(n):
        for j in range(n):
            if i == j: continue
            score += graph[team[i]][team[j]]

    return score

if __name__ == '__main__':
    INF = 10 ** 10
    answer = INF
    N = int(input())
    R = N // 2
    graph = [list(map(int, input().strip().split(' '))) for _ in range(N)]
    people = set([ x for x in range(N)])
    combinations = []

    combination(0, 0, set())

    for startTeam in combinations:
        linkTeam = people - startTeam
        answer = min(answer, abs(getScore(startTeam) - getScore(linkTeam)))

    print(answer)