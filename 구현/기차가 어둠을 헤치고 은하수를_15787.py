N, M = map(int,input().split())
trains = [set([]) for _ in range(N)]

for _ in range(M):
    command=list(map(int, input().split()))
    if len(command) == 3 :
        a,b,c = command
    else:
        a,b = command

    if a == 1:
        trains[b-1].add(c)
    elif a == 2:
        trains[b-1].discard(c)
    elif a == 3:
        trains[b-1].pop()
        trains[b-1].insert(0,'0')
    else:
        trains[b-1].pop(0)
        trains[b-1].append('0')

logs=["".join(trains[0])]
passed=1
for i in range(1,N):
    if "".join(trains[i]) not in logs:
        passed+=1
        logs.append("".join(trains[i]))

print(passed)