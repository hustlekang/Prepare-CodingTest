from itertools import permutations

def solution(str):
    cnt = 0
    numbers = []
    for r in range(1, len(str) + 1):
        picked = list(permutations(str, r))
        for pick in picked:
            numbers.append(int("".join(pick)))
    numbers = list(set(numbers))

    for number in numbers:
        isPrime = True
        if number == 1 or number == 0:
            continue
        for i in range(1, number + 1):
            if number % i == 0:
                if i not in [1, number]:
                    isPrime = False
                    break
        if isPrime:
            cnt += 1

    answer = cnt
    return answer