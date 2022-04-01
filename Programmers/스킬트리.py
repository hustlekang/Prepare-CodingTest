def solution(skill, skill_trees):
    cnt = 0
    for skillTree in skill_trees:
        idx = [100] * len(skill)  # 스킬이 없으면 인덱스를 100으로 본다
        for i in range(len(skill)): #각 스킬들의 인덱스를 기록
            if skill[i] in skillTree:
                idx[i] = skillTree.index(skill[i])

        changed = sorted(idx)
        if changed == idx:  # 스킬들의 인덱스를 정렬해도 그대로여야 스킬을 순서대로 찍은 것
            cnt += 1

    answer = cnt
    return answer