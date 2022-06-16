def solution(n):
    partSum = 0
    end = 1
    cnt = 0

    for start in range(1, n + 1):
        while partSum < n:
            partSum += end
            end += 1
        if partSum == n:
            cnt += 1
        partSum -= start

    return cnt