def solution(s):
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}
    length = len(s)
    answer = ''
    idx = 0
    temp = ''
    while idx < length:
        if s[idx].isdigit():
            if temp != '':
                answer += dic[temp]
                temp = ''
            answer += str(s[idx])
        else:
            if temp in dic.keys():
                answer += dic[temp]
                temp = ''
            temp += s[idx]
        idx += 1
    if temp !='':
        answer += dic[temp]  # 남아있는것 추가

    return int(answer)