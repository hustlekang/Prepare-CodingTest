from collections import defaultdict
import sys
dic = defaultdict(int)

while True:
    species=sys.stdin.readline().strip()
    if not species:
        break
    dic[species]+=1

for species in sorted(dic.keys()):
    print("{} {:.4f}".format(species,dic[species]/sum(dic.values())*100))