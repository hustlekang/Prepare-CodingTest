n,target = map(int,input().split())
numbers=list(map(int,input().split()))
end=0
tempSum=0
cnt=0
for start in range(n):
    while tempSum<target and end<n:
        tempSum+=numbers[end]
        end+=1
    if tempSum==target:
        cnt+=1
    tempSum-=numbers[start]

print(cnt)