T=int(input())
pop_index= {True : -1, False : 0}
for _ in range(T):
    isError = False
    isReversed = False
    commands = input().strip()
    n = int(input())
    arr = input().strip()

    if arr == '[]':
        if 'D' in commands:
            isError = True

    if not isError:
        arr = arr.split(',')
        arr[0] = arr[0][1:]
        arr[-1] = arr[-1][:-1]

        for command in commands:
            if command == 'R':
                isReversed = not isReversed
            else:
                if not arr:
                    isError=True
                    break
                arr.pop(pop_index[isReversed])

    if isError:
        print('error')
    else:
        if isReversed:
            arr = arr[::-1]
        print("["+",".join(arr)+"]")