from collections import defaultdict

def distanceBetweenTwoPoints(arr,k,type):
    # 문자의 인덱스가 정렬되있기 때문에 두 점에서 거리만 구하면 됨
    if type == 'shortest':
        distance = float('inf')
        for start in range(len(arr)-k+1):
            d= abs(arr[start]-arr[start+k-1])+1
            distance = min(d,distance)
    else:
        distance = float('-inf')
        for start in range(len(arr)-k+1):
            d= abs(arr[start]-arr[start+k-1])+1
            distance = max(d,distance)

    return distance

T = int(input())
for _ in range(T):
    W=input().strip() # 문자열
    K=int(input()) # 갯수
    shortest_distance=float('inf')
    longest_distance = float('-inf')
    dic = defaultdict(list)

    for idx,char in enumerate(W):
        dic[char].append(idx)

    for char in dic.keys():
        if len(dic[char]) >= K:
            shortest_distance = min(shortest_distance,distanceBetweenTwoPoints(dic[char],K,'shortest'))
            longest_distance = max(longest_distance,distanceBetweenTwoPoints(dic[char],K,'longest'))

    if shortest_distance != float('inf') and longest_distance != float('-inf'):
        print(shortest_distance,longest_distance)
    else:
        print(-1)