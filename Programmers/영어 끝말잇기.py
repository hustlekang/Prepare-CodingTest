def solution(n, words):
    answer = [0,0]
    already=[]
    for i in range(len(words)):
        if already:
            if words[i] in already or already[-1][-1] != words[i][0]:
                answer=[i%n+1,i//n+1]
                break
        already.append(words[i])
    return answer