from math import ceil

def solution(n, a, b):
    round = 1
    if a > b:
        a, b = b, a

    if b - a == 1 and a % 2 == 1:  # 1라운드에 끝나려면 (홀수,홀수+1) 이어야함
        return round

    while True:
        a = ceil(a / 2)
        b = ceil(b / 2)
        round += 1
        if b - a == 1 and a % 2 == 1:
            break

    return round