str=input().strip()
answer=list(str)
isTag=False
index=[]

for i in range(len(str)):
    char = str[i]
    if char in ['<','>']:
        isTag = not isTag
        if index:
            reverse = str[index[0]:index[-1] + 1][::-1]
            for i in range(index[0], index[-1] + 1):
                answer[i] = reverse[i - index[0]]
            index.clear()
        continue

    if isTag:
        continue

    if char==" ":
        reverse=str[index[0]:index[-1]+1][::-1]
        for i in range(index[0],index[-1]+1):
            answer[i] = reverse[i-index[0]]
        index.clear()

    else:
        index.append(i)

if index:
    reverse = str[index[0]:index[-1] + 1][::-1]
    for i in range(index[0], index[-1] + 1):
        answer[i] = reverse[i - index[0]]

print("".join(answer))