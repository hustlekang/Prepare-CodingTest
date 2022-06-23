from collections import defaultdict
N=int(input())
dic=defaultdict(int)
for _ in range(N):
    dic[input().strip().split('.')[1]]+=1

for name in sorted(dic.keys()):
    print('{} {}'.format(name,dic[name]))