def solution(citations):
    left = 0
    right = 1000
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cntOver = 0
        cntUnder = 0
        for citation in citations:
            if citation >= mid:
                cntOver += 1
            else:
                cntUnder += 1

        if cntOver >= mid and cntUnder <= mid:
            left = mid + 1
            answer = max(answer, mid)
        else:
            right = mid - 1

    return answer