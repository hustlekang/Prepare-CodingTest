from collections import deque

def solution(begin, target, words):
    n=len(begin)
    answer = 100
    visit={}
    for word in words:
        visit[word]=100
    queue=deque([(begin,0)]) # (단어,변화횟수)
    while queue:
        word,change=queue.popleft()
        if word == target:
            answer = min(answer,change)
            continue

        for nextWord in words:
            same=0
            for i in range(n):
                if word[i]==nextWord[i]:
                    same+=1
            if same==n-1 and (visit[nextWord]==100 or change+1<=visit[nextWord] ): # 한 개만 다른 단어
                queue.append((nextWord,change+1))
                visit[nextWord]=change+1

    if answer==100:
        answer=0

    return answer