T=int(input())
for _ in range(T):
    answer='YES'
    phoneBook=[]
    n=int(input())
    for _ in range(n):
        phoneBook.append(input().strip())

    phoneBook.sort()
    for i in range(n-1):
        if phoneBook[i+1].startswith(phoneBook[i]):
            answer='NO'
            break

    print(answer)