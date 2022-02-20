import math
#에라토네스의 체
n=int(input())
array=[True for i in range(n+1)]
numbers=[]
for i in range(2,int(math.sqrt(n))+1):
    if array[i]:
        j=2
        while i * j <=n:
            array[i*j] = False
            j+=1

for i in range(2,n+1):
    if array[i]:numbers.append(i)

#투포인터
if n==1:
    print(0)
else:
    cnt=0
    end=0
    tempSum=0
    lengthNumbers=len(numbers)
    for start in range(lengthNumbers):
        while tempSum<n and end<lengthNumbers:
            tempSum+=numbers[end]
            end+=1
        if tempSum==n:
            cnt+=1
        tempSum-=numbers[start]

    print(cnt)