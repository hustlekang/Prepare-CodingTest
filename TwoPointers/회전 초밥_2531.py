#pypy3 일때 정답, python3은 시간초과
n, d, k, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
answer = 0
end = 0
partArr = []
for start in range(n):
    while (len(partArr) < k):
        partArr.append(arr[end % n])
        end += 1

    temp = list(set(partArr))
    if c not in temp:
        temp.append(c)
    answer = max(answer, len(temp))
    partArr.pop(0)

print(answer)