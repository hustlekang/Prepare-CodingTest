# before -> after 로 문자를 추가하는 로직은 경우의 수가 너무 많아져서 시간 초과
# after -> before 로 문자를 삭제해가면 경우의 수가 훨씬 줄어듬

from collections import deque

def shorten(string,length):
    shortenString = []
    if string[0] == 'B':
        shortenString.append(string[length:0:-1])
    if string[-1] == 'A':
        shortenString.append(string[:-1])

    return shortenString

before = input().strip()
after = input().strip()
beforeLength = len(before)
init  = (after,len(after))
queue = deque([init])
answer = 0

while queue:
    string,length = queue.popleft()

    if length == beforeLength:
        if string == before:
            answer = 1
            break
        continue

    for newString in shorten(string,length):
        queue.append((newString,length-1))

print(answer)