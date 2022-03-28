def solution(msg):
    answer=[]
    dic = {}
    for i in range(65,91):
        dic[chr(i)]=i-64

    maxLength=1
    number=27
    i=0
    isFinish=False
    while(True):
        partStr=msg[i:i+maxLength]
        print('현재문자',partStr)
        for j in range(len(partStr)):
            if partStr[:len(partStr)-j] in dic.keys():
                answer.append(dic[partStr[:len(partStr)-j]]) #가장 긴 문자의 번호 추가
                print('{}가 사전에있음'.format(partStr[:len(partStr)-j]))
                if i+len(partStr)-j >=len(msg):
                    isFinish=True
                    break

                newWord=partStr[:len(partStr)-j]+msg[i+len(partStr)-j] # 새롭게 추가할 녀석
                dic[newWord]=number
                print('dic에 [{}]={}추가'.format(newWord,number))
                number+=1
                maxLength=max(len(newWord),maxLength)
                i+=len(partStr[:len(partStr)-j])
                break

        if isFinish:
            break

    return answer