from itertools import permutations

def solution(k, dungeons):
    answer = 0
    orders = list(permutations(dungeons))
    for order in orders:
        hp = k
        cnt = 0
        for dungeon in order:
            if hp < dungeon[0]:
                break
            hp -= dungeon[1]
            cnt += 1
        answer = max(answer, cnt)
    return answer