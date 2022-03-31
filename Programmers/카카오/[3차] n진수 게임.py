def trans(number, notation):
    reverseAnswer = ''
    while (True):
        if number // notation == 0:
            word=str(number)
            if number>=10:
                if number==10:
                    word='A'
                elif number==11:
                    word='B'
                elif number==12:
                    word='C'
                elif number==13:
                    word='D'
                elif number==14:
                    word='E'
                elif number==15:
                    word='F'

            reverseAnswer += word
            break

        word=str(number % notation)
        if notation>=10:
            if number % notation == 10:
                word = 'A'
            elif number % notation == 11:
                word = 'B'
            elif number % notation == 12:
                word = 'C'
            elif number % notation == 13:
                word = 'D'
            elif number % notation == 14:
                word = 'E'
            elif number % notation == 15:
                word = 'F'
        reverseAnswer += word
        number = number // notation
    return reverseAnswer[::-1]

def solution(n, t, m, p):
    answer=''
    indexes=[]
    list=[]
    k=0
    while len(indexes)<t:
        indexes.append((p+k*m)-1)
        k+=1

    number=0
    while len(list)<=indexes[-1]:
        if number>=n: #한개씩 끊어서 넣어야함
            for x in trans(number, n):
                list.append(x)

        else:
            list.append(trans(number, n))

        number+=1

    for idx in indexes:
        answer+=list[idx]

    return answer