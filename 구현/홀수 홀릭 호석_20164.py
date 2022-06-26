def solution(number,cnt):
    global cnt_max,cnt_min
    length = len(number)

    for char in number:
        if int(char)%2==1:
            cnt+=1

    if length == 1:
        cnt_max = max(cnt_max,cnt)
        cnt_min = min(cnt_min,cnt)
        return

    if length == 2:
        solution(str(int(number[0])+int(number[1])),cnt)
    else:
        for i in range(1,length-1):
            for j in range(i+1,length):
                merged=str(int(number[:i])+int(number[i:j])+int(number[j:]))
                solution(merged,cnt)

N=int(input())
cnt_max=float('-inf')
cnt_min=float('inf')
solution(str(N),0)
print(cnt_min,cnt_max)