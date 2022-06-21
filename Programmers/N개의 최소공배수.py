def solution(arr):
    answer = max(arr)
    keepCalculate = True
    while keepCalculate:
        isOk = True
        for number in arr:
            if answer % number != 0:
                isOk = False
        if isOk:
            keepCalculate = False
        else:
            answer += 1

    return answer