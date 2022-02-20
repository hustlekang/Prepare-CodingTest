import math

isPrime = [True for _ in range(1001)]
isPrime[1]=False
for i in range(2, int(math.sqrt(1000)) + 1):
    if isPrime[i]:
        j = 2
        while (i * j <= 1000):
            isPrime[i * j] = False
            j += 1

trial = int(input())
cnt = 0
for number in map(int, input().split()):
    if isPrime[number]: cnt += 1

print(cnt)