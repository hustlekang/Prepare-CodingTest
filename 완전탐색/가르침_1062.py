import sys
from itertools import combinations
input = sys.stdin.readline

# 단어에 포함된 알파벳을 집합으로 만들어서 부분집합인지로 구하는 센스
def countReadableWord(readableAlpha, words):
    cnt = 0
    for word in words:
        if word.issubset(readableAlpha):
            cnt += 1
    return cnt

if __name__ == '__main__':
    N, K = map(int, input().split(' '))
    if K < 5:
        print(0)
        exit()

    K -= 5
    answer = 0
    words = []
    alphabets = set()
    must = set(['a','n','t','i','c'])

    for _ in range(N):
        word = set(input().strip()) - must
        words.append(word)
        alphabets |= word

    if len(alphabets) == 0:
        print(len(words))
        exit()

    # 조합에서 전체 개수보다 많이 뽑을 순 없음
    if len(alphabets) < K:
        K = len(alphabets)

    for combi in combinations(alphabets, K):
        readableAlpha = set(combi)
        answer = max(answer, countReadableWord(readableAlpha,words))

    print(answer)