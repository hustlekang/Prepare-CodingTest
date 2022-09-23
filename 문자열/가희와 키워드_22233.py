import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    keywords = set()
    for _ in range(N):
        keywords.add(input().strip())
    
    cnt = len(keywords)
    for _ in range(M):
        words = input().strip().split(',')
        for word in words:
            if word in keywords:
                keywords.discard(word)
                cnt -= 1

        print(cnt)