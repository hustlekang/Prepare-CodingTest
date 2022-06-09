def solution(n):
    arr = []
    for i in range(1, n + 1):
        temp = [-1] * i
        arr.append(temp)

    number = 1
    x, y = 0, 0
    while True:
        if number > n * (n + 1) / 2:
            break
        while True: # 아래로 내려가는
            arr[x][y] = number
            x += 1
            number += 1
            if x == n or arr[x][y] != -1:
                x -= 1
                break
        y+=1

        if number > n * (n + 1) / 2:
            break
        while True: # 옆으로 가는
            arr[x][y] = number
            y += 1
            number += 1
            if y == n or arr[x][y] != -1:
                y -= 1
                break

        x -= 1
        y -= 1

        if number > n * (n + 1) / 2:
            break
        while True: # 위로 가는
            arr[x][y] = number
            x -= 1
            y -= 1
            number += 1
            if arr[x][y] != -1:
                x += 1
                y += 1
                break
        x+=1

    return sum(arr,[])