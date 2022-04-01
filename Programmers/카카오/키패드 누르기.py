def solution(numbers, hand):
    answer = ''
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2),
              'star': (3, 0), 0: (3, 1), 'sharp': (3, 2)}
    locationL = (3, 0)
    locationR = (3, 2)

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            locationL = keypad[number]

        elif number in [3, 6, 9]:
            answer += 'R'
            locationR = keypad[number]

        else:
            x, y = keypad[number]
            distanceL = abs(x - locationL[0]) + abs(y - locationL[1])
            distanceR = abs(x - locationR[0]) + abs(y - locationR[1])

            if distanceL == distanceR:  # 주손으로 이동
                if hand == 'right':
                    answer += 'R'
                    locationR = keypad[number]
                else:
                    answer += 'L'
                    locationL = keypad[number]

            elif distanceL < distanceR: #왼손이 더 가까우면 왼손 이동
                answer += 'L'
                locationL = keypad[number]
            else:
                answer += 'R'
                locationR = keypad[number]

    return answer