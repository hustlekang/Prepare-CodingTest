def solution(people, limit):
    people.sort(reverse=True)
    isrescued = [False] * len(people)
    cnt = 0
    end = -1

    for start in range(len(people)):
        if not isrescued[start]:
            if people[start] + people[end] <= limit:
                isrescued[start] = True
                isrescued[end] = True
                end -= 1
            else:
                isrescued[start] = True
            cnt += 1

    return cnt