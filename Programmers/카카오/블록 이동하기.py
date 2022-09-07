from collections import deque

def rotate(x1,y1,x2,y2,board):
    n = len(board)
    rotated = []
    if x1 == x2: # 로봇이 가로로 있을 때
        r_x, r_y = x1, max(y1, y2) # 로봇의 오른쪽 부분 좌표
        l_x, l_y = x1, min(y1, y2) # 로봇의 왼쪽 부분 좌표

        if l_x + 1 < n and board[l_x+1][l_y] == 0 and board[r_x+1][r_y] == 0: # 오른쪽 기준 아래로 회전
            rotated.append([(r_x,r_y),(r_x+1,r_y)])
        if 0 <= l_x - 1 and board[l_x-1][l_y] == 0 and board[r_x-1][r_y] == 0: # 오른쪽 기준 위로 회전
            rotated.append([(r_x,r_y),(r_x-1,r_y)])
        if l_x + 1 < n and board[l_x+1][l_y] == 0 and board[r_x+1][r_y] == 0: # 왼쪽 기준 아래로 회전
            rotated.append([(l_x,l_y),(l_x+1,l_y)])
        if 0 <= l_x - 1 and board[l_x-1][l_y] == 0 and board[r_x-1][r_y] == 0: # 왼쪽 기준 위로 회전
            rotated.append([(l_x,l_y),(l_x-1,l_y)])

    else: # 로봇이 세로로 있을 때
        d_x, d_y = max(x1, x2), y1 # 로봇의 아래쪽 부분 좌표
        u_x, u_y = min(x1, x2), y1 # 로봇의 위쪽 부분 좌표

        if u_y + 1 < n and board[u_x][u_y+1] == 0 and board[d_x][d_y+1] == 0: # 아래 기준 오른쪽 회전
            rotated.append([(d_x,d_y),(d_x,d_y+1)])
        if 0 <= u_y - 1 and board[u_x][u_y-1] == 0 and board[d_x][d_y-1] == 0: # 아래 기준 왼쪽 회전
            rotated.append([(d_x,d_y), (d_x,d_y-1)])
        if 0 <= u_y - 1 and board[u_x][u_y-1] == 0 and board[d_x][d_y-1] == 0: # 위 기준 왼쪽 회전
            rotated.append([(u_x,u_y), (u_x,u_y-1)])
        if u_y + 1 < n and board[u_x][u_y+1] == 0 and board[d_x][d_y+1] == 0: # 위 기준 오른쪽 회전
            rotated.append([(u_x,u_y), (u_x,u_y+1)])

    return rotated

def solution(board):
    answer = -1
    n = len(board)
    visit = [{(0,0),(0,1)}] # {(x1,y1),(x2,y2)} 의 형태로 방문을 확인
    init = (0, 0, 0, 1, 0) # x1, y1, x2, y2, cnt
    queue = deque([init])

    while queue:
        x1, y1, x2, y2, cnt = queue.popleft()
        # 로봇의 두 좌표중 하나라도 끝점에 도달하면
        if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
            answer = cnt
            break

        for dx,dy in zip([0,0,1,-1],[1,-1,0,0]): # 이동 가능한 좌표들 큐에 추가
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy
            # 새로운 두 좌표가 board 범위 내에 있고 빈 칸이고 방문한 적이 없을 때
            if 0<= nx1 < n and 0<= ny1 < n and 0<= nx2 < n and 0<= ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0 and {(nx1,ny1),(nx2,ny2)} not in visit:
                visit.append({(nx1, ny1), (nx2, ny2)})
                queue.append((nx1, ny1, nx2, ny2, cnt + 1))

        for locationX,locationY in rotate(x1,y1,x2,y2,board): # 회전한 좌표들 큐에 추가
            rx1, ry1 = locationX
            rx2, ry2 = locationY
            if {(rx1,ry1),(rx2,ry2)} not in visit: # 방문한 적이 없을 때
                visit.append({(rx1, ry1), (rx2, ry2)})
                queue.append((rx1, ry1, rx2, ry2, cnt + 1))

    return answer


######################### 시간초과 , visit의 차이점
from collections import deque

def rotate(x1,y1,x2,y2,board):
    n = len(board)
    rotated = []
    if x1 == x2: # 로봇이 가로로 있을 때
        r_x, r_y = x1, max(y1, y2) # 로봇의 오른쪽 부분 좌표
        l_x, l_y = x1, min(y1, y2) # 로봇의 왼쪽 부분 좌표

        if l_x + 1 < n and board[l_x+1][l_y] == 0 and board[r_x+1][r_y] == 0: # 오른쪽 기준 아래로 회전
            rotated.append([(r_x,r_y),(r_x+1,r_y)])
        if 0 <= l_x - 1 and board[l_x-1][l_y] == 0 and board[r_x-1][r_y] == 0: # 오른쪽 기준 위로 회전
            rotated.append([(r_x,r_y),(r_x-1,r_y)])
        if l_x + 1 < n and board[l_x+1][l_y] == 0 and board[r_x+1][r_y] == 0: # 왼쪽 기준 아래로 회전
            rotated.append([(l_x,l_y),(l_x+1,l_y)])
        if 0 <= l_x - 1 and board[l_x-1][l_y] == 0 and board[r_x-1][r_y] == 0: # 왼쪽 기준 위로 회전
            rotated.append([(l_x,l_y),(l_x-1,l_y)])

    else: # 로봇이 세로로 있을 때
        d_x, d_y = max(x1, x2), y1 # 로봇의 아래쪽 부분 좌표
        u_x, u_y = min(x1, x2), y1 # 로봇의 위쪽 부분 좌표

        if u_y + 1 < n and board[u_x][u_y+1] == 0 and board[d_x][d_y+1] == 0: # 아래 기준 오른쪽 회전
            rotated.append([(d_x,d_y),(d_x,d_y+1)])
        if 0 <= u_y - 1 and board[u_x][u_y-1] == 0 and board[d_x][d_y-1] == 0: # 아래 기준 왼쪽 회전
            rotated.append([(d_x,d_y), (d_x,d_y-1)])
        if 0 <= u_y - 1 and board[u_x][u_y-1] == 0 and board[d_x][d_y-1] == 0: # 위 기준 왼쪽 회전
            rotated.append([(u_x,u_y), (u_x,u_y-1)])
        if u_y + 1 < n and board[u_x][u_y+1] == 0 and board[d_x][d_y+1] == 0: # 위 기준 오른쪽 회전
            rotated.append([(u_x,u_y), (u_x,u_y+1)])

    return rotated

def solution(board):
    INF = 10**8
    answer = INF
    n = len(board)
    visit = [[INF] * n for _ in range(n)]
    visit[0][0] = 0
    visit[0][1] = 0
    init = (0, 0, 0, 1, 0) # x1, y1, x2, y2, cnt
    queue = deque([init])

    while queue:
        x1, y1, x2, y2, cnt = queue.popleft()

        # 로봇의 두 좌표중 하나라도 끝점에 도달하면
        if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
            answer = min(answer, cnt)
            continue

        for dx,dy in zip([0,0,1,-1],[1,-1,0,0]): # 회전 안하고 이동 가능한 곳으로 이동한 좌표 큐에 삽입
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy
            # 새로운 두 좌표가 board 범위 내에 있고 빈 칸이고, visit 값이 작을 때만 이동
            if 0<= nx1 < n and 0<= ny1 < n and 0<= nx2 < n and 0<= ny2 < n and board[nx1][ny1] == 0 and board[nx2][ny2] == 0 and (cnt + 1 < visit[nx1][ny1] or cnt + 1 < visit[nx2][ny2]):
                if cnt + 1 < visit[nx1][ny1]:
                    visit[nx1][ny1] = cnt + 1
                if cnt + 1 < visit[nx2][ny2]:
                    visit[nx2][ny2] = cnt + 1
                queue.append((nx1, ny1, nx2, ny2, cnt + 1))

        for locationX,locationY in rotate(x1,y1,x2,y2,board): # 회전만 해서 큐에 삽입
            rx1, ry1 = locationX
            rx2, ry2 = locationY
            queue.append((rx1, ry1, rx2, ry2, cnt + 1))

    return answer