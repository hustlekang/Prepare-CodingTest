# ex) [1, 3, 5, 4, 2]
# 1) 크기 순으로 정렬 했을 때 [1, 3, 5, 4, 2] 다음 순서는
# 2) 맨 오른쪽부터 점점 증가하다가 감소하는 구간을 기준으로 나눈다 arr1 = [1, 3] , arr2 = [5, 4, 2]
# 3) arr1[-1] = 3 보다 큰 최소값을 arr2 에서 찾는다  4
# 4) arr[2]에서 찾은 4를 빼서 arr[-1]자리에 넣어주고, arr[-1]에 있던 3을 arr[2]에 추가한다
#    arr1 = [1, 4] , arr2 = [5, 2, 3]
# 5) arr2를 정렬해서 arr2 = [2, 3, 5]
# 6) arr1과 arr2를 연결
#    [1, 4] + [5, 2, 3] = [1, 4, 5, 2, 3]

T=int(input())
for _ in range(T):
    word=list(input().strip())
    length=len(word)

    if sorted(word,reverse=True)==word: # 사전 순으로 마지막이면 바로 출력
        print("".join(word))
        continue

    idx = length-1 # idx는 맨 마지막부터 왼쪽으로 탐색
    while idx>0:
        if word[idx-1] < word[idx]: # 왼쪽으로 가다가 감소하는 구간을 캐치
            break
        idx-=1

    part=word[idx:] # idx 부터 값 중에서 [idx-1] (감소하는 구간) 보다 큰 값중 가장 작은 값을 찾아야함
    part.sort() # 정렬하고
    left=0
    right=len(part)-1
    target_idx=100 # 불가능한 인덱스
    while left<=right: # 이분 탐색으로 idx-1 보다 큰 값 중 min 을 찾는다
        mid = (left+right)//2
        if word[idx-1] < part[mid]:
            target_idx=min(target_idx,mid)
            right = mid - 1
        else:
            left = mid + 1

    temp=word[idx-1]
    word[idx-1]=part[target_idx] # 감소하는 그 구간에 찾은 값을 넣어주고
    part.pop(target_idx)
    part.append(temp) # 그 구간에 있던 값을 뒷부분에 포함시키고
    part.sort() # 정렬해서

    for i in range(idx,length): # 다시 이어붙친다
        word[i]=part[i-idx]

    print("".join(word))