from collections import defaultdict

N=int(input())
schedule = defaultdict(int)
for _ in range(N):
    start,end=map(int,input().split())
    for day in range(start,end+1):
        schedule[day]+=1

answer=0
width=0
height=0

for day in range(1,365+1):
    if schedule[day] == 0:
        if width * height !=0: # day 전 날짜에 일정이 있을 시
            answer += width * height
            width=0
            height=0
    else:
        width+=1
        height=max(height,schedule[day])

answer += width * height

print(answer)