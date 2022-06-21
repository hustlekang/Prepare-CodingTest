def solution(s):
    cnt = 0
    removed = 0
    while s != '1':
        new = s.replace("0", '')
        removed += (len(s) - len(new))
        s = new
        s = bin(len(s))[2:]
        cnt += 1

    answer = [cnt, removed]
    return answer