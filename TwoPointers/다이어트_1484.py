g=int(input())
rememberWeight=[x**2 for x in range(1,100000)]
answer=[]
for rememberW in rememberWeight:
    if ((g+rememberW)**(1/2))%1==0 :
        answer.append(int((g+rememberW)**(1/2)))

if len(answer)==0:
    print(-1)
else:
    for answer in answer:
        print(answer)