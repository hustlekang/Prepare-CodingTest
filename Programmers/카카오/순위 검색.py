def solution(info, queries):
    answer = []
    peopleByType={}

    for lan in ['python','cpp','java','-']:
        for type in ['backend','frontend','-']:
            for career in ['junior','senior','-']:
                for food in ['chicken','pizza','-']:
                    peopleByType[lan+type+career+food]=[]

    for person in info:
        lan, type, career, food, score = person.split(' ')
        for l in [lan,'-']:
            for t in [type,'-']:
                for c in [career,'-']:
                    for f in [food,'-']:
                        peopleByType[l+t+c+f].append(int(score))

    for key in peopleByType.keys(): # sorted는 시간초과, sort는 통과
        peopleByType[key].sort()
    
    for query in queries:
        lan, type, career, foodAndScore = query.split(' and ')
        food, score = foodAndScore.split(' ')
        people = peopleByType[lan + type + career + food]
        #people=sorted(peopleByType[lan + type + career + food])
        left = 0
        right = len(people)-1
        result=0
        while left<=right:
            mid=(left+right)//2
            if people[mid]>=int(score):
                result = max(result,len(people)-mid)
                right = mid-1
            else:
                left = mid + 1

        answer.append(result)

    return answer