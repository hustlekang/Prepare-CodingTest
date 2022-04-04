def solution(s):
    arr = s[1:-1].split('},')
    arr[-1] = arr[-1][:-1]
    for i in range(len(arr)):
        arr[i] = arr[i][1:]
    arr.sort(key=lambda x: len(x)) #arr는 원소의 갯수가 1개인 것부터 차례대로 정렬됨

    for i in range(len(arr)):
        arr[i] = set(map(int, arr[i].split(','))) #set로 만들어준다

    answer = []
    for i in enumerate(arr): # arr = [{1},{1,2} ,{1,4,2}] 일때 앞에 집합꺼 뺀 나머지가 그 다음 수(124)
        if i[0] == 0:
            answer.append(list(i[1])[0]) #맨처음은 바로삽입 , set는 인덱스 접근 불가이므로 list로 만듬
        else:
            answer.append(list(i[1] - arr[i[0] - 1])[0]) #앞에꺼 빼줌

    return answer