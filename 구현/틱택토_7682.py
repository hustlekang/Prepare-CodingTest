def isValid(str):
    p1_cnt = 0
    p2_cnt = 0
    blank = 0

    for each in str:
        if each == 'X':
            p1_cnt += 1
        elif each == 'O':
            p2_cnt += 1
        else:
            blank += 1

    ssangSam = set(['OXOXXXOXO', 'XOOXXXXOO', 'OOXXXXOOX', 'OXOOXOXXX', 'XXXOXOOXO'])
    idxes = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    p1_bingo = 0
    p2_bingo = 0

    for i, j, k in idxes:
        if str[i] == str[j] == str[k]:
            if str[i] == 'X':
                p1_bingo += 1
            elif str[i] == 'O':
                p2_bingo += 1

    # 두번째 사람이 이길때
    if p1_bingo == 0 and p2_bingo == 1 and p1_cnt == p2_cnt:
        return True

    # 첫번째 사람이 이길 때
    if p2_cnt + 1 == p1_cnt:
        if p1_bingo == 1 and p2_bingo == 0:
            return True
        if str in ssangSam: # 마지막 한개를 놨는데 쌍삼일 수 있음
            return True

    # 판이 꽉찰 때
    if p1_cnt == 5 and p2_cnt == 4 and p2_bingo == 0:
        return True

    # 아니면 불가능
    return False


if __name__ == '__main__':
    while True:
        str = input().strip()
        if str == 'end':
            break
        print('valid' if isValid(str) else 'invalid')