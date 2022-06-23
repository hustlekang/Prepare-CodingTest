# stack 을 문자열로 하고 += 하면 시간초과, 배열로 하고 append 하면 통과
str=input().strip()
boom=input().strip()
stack=[]

for char in str:
    stack.append(char)
    if  char == boom[-1] and "".join(stack[-len(boom):]) == boom:
        for _ in range(len(boom)):
            stack.pop()

if not stack:
    print('FRULA')
else:
    print("".join(stack))