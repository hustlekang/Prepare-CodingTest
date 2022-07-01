str=input().strip()
length=len(str)
isOdd = length%2==1
answer= None

if length ==1 or str.count(str[0])==length: # 한자리거나 모두다 같은 문자면 불가능
    answer=-1
else:
    if isOdd:
        if str[:length//2+1] != str[length//2:][::-1]: # 대칭이 아니면
            answer = length
        else: # 대칭일 때 문자열 한개만 뺴주면 무조건 대칭 아님
            answer = length -1
    else:
        if str[:length//2] != str[length//2:][::-1]:
            answer = length
        else:
            answer = length - 1

print(answer)