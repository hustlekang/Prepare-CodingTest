from collections import deque

def solution(numbers, target):
    answer=0
    l=len(numbers)
    candidates=[]
    queue=deque(['-','+'])

    while queue:
        v=queue.popleft()
        if len(v)==l:
            candidates.append(v)
            continue
        queue.append(v+'+')
        queue.append(v+'-')

    for plusminus in candidates:
        result=0
        for i in range(l):
            unknown=plusminus[i]
            if unknown=='+':
                result+=numbers[i]
            else:
                result-=numbers[i]

        if result==target:
            answer+=1

    return answer