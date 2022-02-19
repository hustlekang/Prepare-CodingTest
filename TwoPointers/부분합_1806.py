import sys
length,target=map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
start=0
end=0
tempSum=0
answer=100000
if target==0:
    print(1)
else:
    for start in range(length):
        while tempSum<target and end<length:
            tempSum+=arr[end]
            end+=1

        if tempSum>=target:
            answer=min(answer,end-start)

        tempSum-=arr[start]

    if answer==100000:
        answer=0

    print(answer)