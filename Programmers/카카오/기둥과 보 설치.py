def check(x, y, a, built):
    if a == 0: # 기둥
        if y == 0 or (x-1, y, 1) in built or (x, y, 1) in built or (x, y-1, 0) in built: # 문제 조건 순서대로
            return True
        return False
    else: # 보
        if (x, y-1, 0) in built or (x + 1, y - 1, 0) in built or ( (x - 1, y, 1) in built and (x + 1, y, 1) in built): # 문제 조건 순서대로
            return True
        return False

def solution(n, build_frame):
    built = set()

    for x, y, a, b in build_frame:
        if b == 1: # 구조물을 설치
            if check(x, y, a, built):
                built.add((x, y, a))
        else: # 구조물 삭제
            built.remove((x, y, a)) # 먼저 없애보고
            for x2, y2, a2 in built: # 현재 모든 구조물에 대해 조건을 만족하는지 체크
                if not check(x2, y2, a2, built): # 없애서 만족 안하면 다시 복구
                    built.add((x, y, a))
                    break

    answer = list(built)
    answer.sort(key= lambda x: (x[0], x[1], x[2]))

    return answer