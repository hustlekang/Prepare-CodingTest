def solution(sizes):
    for i in range(len(sizes)):
        card = sizes[i]
        if card[0] > card[1]: #모든 명함을 무조건 긴변이 세로로 오게끔 계속 위에다가 겹쳐서 올리면 면적 최소인 모양
            sizes[i] = [card[1], card[0]] # 가로,세로

    leftMax = max(i[0] for i in sizes)
    rightMax = max(i[1] for i in sizes)
    answer = leftMax * rightMax
    return answer