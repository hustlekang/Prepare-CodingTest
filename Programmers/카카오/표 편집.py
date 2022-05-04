def solution(n, k, cmds):
    table = ['O'] * n
    deleted = []
    select = k
    linkedList = {i: [i - 1, i + 1] for i in range(n)} # 노드번호 : [왼쪽노드번호, 오른쪽노드번호]

    for cmd in cmds:
        command = cmd.split(' ')
        type = command[0]
        d = -1
        if len(command) == 2:
            d = int(command[1])

        if type == 'U':
            for _ in range(d):
                select = linkedList[select][0]

        elif type == 'D':
            for _ in range(d):
                select = linkedList[select][1]

        elif type == 'C':
            deleted.append((select, linkedList[select]))
            table[select] = 'X'
            n_nodeL,n_nodeR = linkedList[select]

            # 연결 상태 변경
            if n_nodeL == -1:
            # if select == 0: 노드 번호로 하면 안되고 연결된 노드로 체킹해야함, 연걸을 끊는건 left,right 노드를 교체함으로써 업데이트 하니 맨 처음 노드는 0번이 아니고 leftnode가 -1인 애임
                linkedList[n_nodeR][0] = -1
            elif n_nodeR == n: # 현재 노드가 맨 오른쪽 노드일 때
                linkedList[n_nodeL][1] = n
            else: # 양 옆에 노드가 있을 때
                linkedList[n_nodeL][1] = n_nodeR
                linkedList[n_nodeR][0] = n_nodeL
            # select 변경
            if n_nodeR != n:
                select = n_nodeR
            else:
                select = n_nodeL

        else:  # Z
            node, [n_nodeL, n_nodeR] = deleted.pop()
            table[node] = 'O'
            linkedList[node] = [n_nodeL, n_nodeR]
            if n_nodeL != -1:
                linkedList[n_nodeL][1] = node
            if n_nodeR != n:
                linkedList[n_nodeR][0] = node

    answer = ''.join(table)

    return answer