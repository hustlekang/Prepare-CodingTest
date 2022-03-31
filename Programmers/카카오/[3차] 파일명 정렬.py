def solution(files):
    willSort = []
    for name in files:
        print("{}일때".format(name))
        index = 0
        while not name[index].isdigit():
            index += 1
        head = name[:index]
        print('head',head)
        numberStartIndex = index
        while (name[index].isdigit()):
            if index - numberStartIndex == 5:
                break
            index += 1
            if index ==len(name): #이부분 없어서 런타임 에러 났었음, 마지막 부분까지 index가 오면 종료해야함 ex) "O00321"
                break
        number = int(name[numberStartIndex:index])

        willSort.append((name, head.lower(), number))

    willSort.sort(key=lambda x: x[2])
    willSort.sort(key=lambda x: x[1])

    return [i[0] for i in willSort]