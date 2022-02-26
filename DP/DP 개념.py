def fibo_bottomUp(n):
    dp=[0]*100
    dp[1]=1
    dp[2]=1
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]


dp=[0]*100
def fibo_topDown(n):
    #탈출조건
    if n==1 or n==2 :
        return 1
    #이미 계산한적이 있다면
    if dp[n]!=0:
        return dp[n]
    #아직 계산 안했다면
    dp[n]=fibo_topDown(n-1)+fibo_topDown(n-2)
    return dp[n]

print(fibo_bottomUp(99))
print(fibo_topDown(99))