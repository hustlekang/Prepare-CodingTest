def solution(m, musicinfos):
    melody = m
    answerList=[]
    answer='(None)'
    order=1
    for song in musicinfos:
        start,end,title,code = song.split(",")

        melody = melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        code = code.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

        duration = (int(end[3:])+ int((int(end[:2])-int(start[:2]))*60)  ) - int(start[3:])
        p=duration//len(code)
        r=duration%len(code)

        fullcode=code*p
        cnt=0
        i=0
        while(cnt<r):
            fullcode+=code[i]
            i += 1
            cnt+=1

        if melody in fullcode:
            answerList.append((title,duration,order))

        order+=1

    if answerList:
        if len(answerList)==1:
            answer=answerList[0][0]
        else:
            answerList.sort(key=lambda x:x[2])
            answerList.sort(key=lambda x:x[1],reverse=True)
            answer = answerList[0][0]

    return answer


##########################
def solution(m, musicinfos):
    answerList=[]
    answer='(None)'
    order=1
    for song in musicinfos:
        melody = m
        start,end,title,code = song.split(",")
        fullcode=''
        duration=0
        codeLength=len(code)-code.count('#')
        duration = (int(end[3:])+ int((int(end[:2])-int(start[:2]))*60)  ) - int(start[3:])

        p=duration//codeLength
        r=duration%codeLength
        fullcode=code*p
        cnt=0
        i=0
        while(cnt<r):
            fullcode+=code[i]
            i += 1
            if code[i]=='#':
                fullcode += code[i]
                i+=1
            cnt+=1


        while melody in fullcode:
            if fullcode.index(melody) + len(melody) <= len(fullcode) - 1 and fullcode[fullcode.index(melody) + len(melody)] == '#':
                fullcode=fullcode[fullcode.index(melody) + len(melody):]
            else:
                answerList.append((title, duration, order))
                break

        order+=1

    if answerList:
        if len(answerList)==1:
            answer=answerList[0][0]
        else:
            answerList.sort(key=lambda x:x[2])
            answerList.sort(key=lambda x:x[1],reverse=True)
            answer = answerList[0][0]

    return answer