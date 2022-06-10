def solution(s):
    words = s.split(' ')
    answer = ''
    for word in words:
        if word == '':
            answer += ' '
        else:
            word = word.lower()
            if word[0].isdigit():
                answer += word + ' '
            else:
                answer += chr(ord(word[0]) - 32) + word[1:] + ' '

    answer = answer[:-1]
    return answer