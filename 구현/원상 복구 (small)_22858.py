N,K = map(int,input().split())
after = list(map(int,input().split()))
control = list(map(int,input().split()))

for _ in range(K):
    recover = [0]*N
    for i in range(N):
        recover[control[i]-1]=after[i]
    after = recover
before = list(map(str,after))

print(" ".join(before))