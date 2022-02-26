n=int(input())
dp=[0]*1001
dp[1]=[1,1,1,1,1,1,1,1,1,1]
for i in range(2,n+1):
    temp=[0]*10
    for j in range(10):
        if j==0:
            temp[j] = sum(dp[i - 1])
        temp[j]=sum(dp[i-1])-sum(dp[i-1][:j])
    dp[i]=temp

print(sum(dp[n])%10007)