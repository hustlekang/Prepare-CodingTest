k = int(input()) # 참가자수
n = int(input()) # 전체 가로줄 수
result = input().strip() #최종 결과
before = [chr(x) for x in range(65,65+k,1)] # 시작 사람 배치
start_idx={}
result_idx={}
for idx,char in enumerate(before):
    start_idx[char]=int(idx*2)
for idx,char in enumerate(result):
    result_idx[char]=int(idx*2)

graph=[[0]*(2*k-1) for _ in range(3+2*(n-1))]
linefirst=[]
lineLast=[]
for char in before:
    linefirst.append(char)
    linefirst.append(0)
linefirst.pop()
for char in list(result):
    lineLast.append(char)
    lineLast.append(0)
lineLast.pop()
graph[0]=linefirst
graph[-1]=lineLast

target_idx=0 # 사다리 배치해야 되는 x인덱스
for i in range(n):
    line=input().strip()
    if '?' == line[0]:
        target_idx=int(2*i)+1
        graph[target_idx]=['?'] * (2 * k - 1)
        continue
    for idx, connect in enumerate(line):
        graph[2*i+1][2*idx+1]=connect

canConnect=True
for start in before:
    # 맨 위에서 부터 아래로 ???지점까지 내려간다
    x1=0
    y1=start_idx[start]
    while x1<target_idx:
        x1+=1
        if y1+2<len(graph[0]) and graph[x1][y1+1]=='-':
            y1+=2
        elif 0<=y1-2 and graph[x1][y1-1] == '-':
            y1-=2

    # 맨 아래에서 위로 ??? 지점까지 올라간다
    x2=len(graph)-1
    y2=result_idx[start]
    while x2>target_idx:
        x2-=1
        if y2+2<len(graph[0]) and graph[x2][y2+1]=='-':
            y2+=2
        elif 0<=y2-2 and graph[x2][y2-1]=='-':
            y2-=2

    if y1==y2: # 같은 위치에서 만났으면 좌,우에 이동가능한 사다리가 있으면 안됨
        graph[x1][y1-1]='*'
        if y1+1<len(graph[0]): # 맨 오른쪽에서 만나면 사다리는 왼쪽밖에 못놓음
            graph[x1][y1+1]='*'
    elif abs(y1-y2)==2: # 하나 엇갈렸으면 사이에 사다리 놓아준다
        graph[x1][(y1+y2)//2]='-'
    else: # 그 이상이라면 해결 불가능
        canConnect=False
        break

answer=''
if not canConnect:
    answer='x'*(k-1)
else:
    for i in range(k-1):
        answer+=graph[target_idx][i*2+1]
    answer=answer.replace('?','*') # 한번도 탐색되지 않은 부분이 있을수도 있음, 그 부분은 사다리 놓을 필요 없으니 *로 바꿔줌
print(answer)