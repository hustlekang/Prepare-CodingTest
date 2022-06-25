N=int(input())
street = input().strip()
parts=0
for i in range(N-1):
    if street[i]=='W' and street[i+1] == 'E':
        parts+=1
answer = parts + 1
print(answer)