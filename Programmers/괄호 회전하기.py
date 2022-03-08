# )}] 만날 시 결국 word의 마지막 자리에 해당 괄호 열리는 ({[ 가 있어야 닫힘 그래서 word[-1]만 보면됨
def solution(s):
    length=len(s)
    answer= 0
    for _ in range(length):
        s = s[1:] + s[0]
        if isRight(s):
            answer+=1

    return answer

def isRight(str):
    word=""
    for i in range(len(str)):
        if word=="":
            word += str[i]
            continue

        if str[i]== ')' :
            if word[-1]=='(':
                word=word[:-1]
            else:
                return False

        elif str[i]=='}':
            if word[-1]=='{':
                word=word[:-1]
            else:
                return False

        elif str[i] == ']':
            if word[-1]=='[':
                word=word[:-1]
            else:
                return False

        else:
            word += str[i]

    if word=='':
        return True
    else:
        return False

##############################################
# ([{)}] 마지막 테스트 케이스 통과 못함
def solution(s):
    length=len(s)
    answer= 0
    for _ in range(length):
        s = s[1:] + s[0]
        if isRight(s):
            answer+=1

    return answer

def isRight(str):
    word=""

    for i in range(len(str)):
        if str[i]== ')' :
            if '(' in word:
                idx=word.index('(')
                word=word[:idx]+word[idx+1:]
            else:
                return False

        elif str[i]=='}':
            if '{' in word:
                idx = word.index('{')
                word = word[:idx] + word[idx + 1:]
            else:
                return False

        elif str[i] == ']':
            if '[' in word:
                idx = word.index('[')
                word = word[:idx] + word[idx + 1:]
            else:
                return False

        else:
            word += str[i]

    if word=='':
        return True
    else:
        return False