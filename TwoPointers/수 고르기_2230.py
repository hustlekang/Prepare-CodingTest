n, atLeastSum = map(int, input().split())
numbers = []
for _ in range(n) : numbers.append(int(input()))
numbers.sort() #sort안해주니 15%에서 틀림

end = 0
answer = 2000000000
for start in range(n):
    while abs(numbers[start] - numbers[end]) < atLeastSum and end < n - 1:
        end += 1

    if abs(numbers[start] - numbers[end]) == atLeastSum:
        answer = abs(numbers[start] - numbers[end])
        break

    elif abs(numbers[start] - numbers[end]) >= atLeastSum:
        answer = min(answer, abs(numbers[start] - numbers[end]))

print(answer)