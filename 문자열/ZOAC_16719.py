if __name__ == '__main__':
    str = input().strip()
    answerList = [str]

    while str != '':
        w = str
        for i in range(len(str)):

            word = str[:i] + str[i + 1:]
            if word < w:
                w = word

        answerList.append(w)
        str = w

    answerList.pop()
    for answer in answerList[::-1]:
        print(answer)