def solution(record):
    log = []
    answer = []
    dic = {}
    for line in record:
        if line.startswith('Enter'):
            type, id, nickname = line.split(' ')
            dic[id] = nickname
            log.append((id, type))
        elif line.startswith('Change'):
            type, id, nickname = line.split(' ')
            dic[id] = nickname
        else:  # Leave
            type, id = line.split(' ')
            log.append((id, type))

    for info in log:
        id, type = info
        if type == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(dic[id]))
        else:
            answer.append('{}님이 나갔습니다.'.format(dic[id]))

    return answer