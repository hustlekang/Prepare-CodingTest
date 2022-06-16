def solution(n):
    cntOfOne = bin(n).count('1')
    number = n + 1
    while True:
        if bin(number).count('1') == cntOfOne:
            answer = number
            break
        number += 1

    return answer