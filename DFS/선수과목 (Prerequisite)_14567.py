import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(node, cnt):
    dp[node] = cnt

    if not connection[node]:
        return

    for nextNode in connection[node]:
        if cnt >= dp[nextNode]:
            dfs(nextNode, cnt + 1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    dp = [1] * (N + 1)
    roots = set([x for x in range(1, N + 1)])
    connection = defaultdict(list)
    visit = [False] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        connection[a].append(b)
        roots.discard(b)

    for root in roots:
        dfs(root, 1)

    print(*dp[1:])