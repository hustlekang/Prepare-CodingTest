# 아래 시간초과 코드보다 160배 빠름
from collections import deque

def solution(bridge_length, weight, truck_weights):
    second=1 #1초 경과한 상태에서 시작, 다리에 첫 트럭을 올려놓고
    totalWeight=truck_weights[0] #맨 처음 트럭만 있으니
    truckOnBridge = 1 #다리위 트럭의 수
    bridge=[truck_weights[0]]+[0]*(bridge_length-1) # [x,0,0,0] 빈공간은 0, 길이는 다리길이만큼
    truck_weights.pop(0) # 첫 트럭은 다리에 올리고 시작하니까 제외
    bridge=deque(bridge) # --->[ 다리 ]---> 왼쪽으로 들어와서 오른쪽으로 나감

    for truck in truck_weights: #truck = 다리에 들어갈 트럭
        while truck+totalWeight>weight or truckOnBridge+1 >bridge_length or bridge[0]!=0 :
            second += 1 # 트럭이 들어올 수 있을 때 까지 시간을 경과시킨다
            bridge.rotate(1) #오른쪽으로 1칸씩 쉬프팅
            out=bridge.popleft() # 맨 오른쪽에 있던애가 맨앞으로 왔으니 얜 빼고
            bridge.appendleft(0)  # 걔 대신 0을 넣어준다
            if out != 0: #다리에서 나간얘가 트럭이라면
                totalWeight-=out # 다리 벗어난얘는 다리 전체 무게에서 뺀다
                truckOnBridge-=1 # 개수도 빼줌

        bridge.popleft() # 맨앞칸에 0을 빼고
        bridge.appendleft(truck) #맨앞에 트럭을 넣어준다
        truckOnBridge+=1
        totalWeight+=truck

    second+=bridge_length #마지막 트럭이 들어가고 for문이 끝나니까 다리 길이만큼 초가 지나야 마지막 트럭이 빠져나감

    return second


print(solution(2, 10, [7, 4, 5, 6]))



############# test case : 5 시간초과##########
## 다리에 있는 트럭의 무게 총합을 sum()으로 구해서 --> 초기 무게 설정 후 트럭이 들어오고 나갈 때마다 갱신
## 다리에 있는 트럭의 갯수를 count()로 다 세니까  --> 초기 갯수 설정 후 트럭이 들어오고 나갈 때마다 갱신

from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = 1
    bridge = [truck_weights[0]] + [0] * (bridge_length - 1)
    truck_weights.pop(0)
    bridge = deque(bridge)  # --->[ 다리 ]---> 왼쪽으로 들어와서 오른쪽으로 나감

    for truck in truck_weights:  # truck = 다리에 들어갈 트럭
        truckOnBridge = bridge_length - bridge.count(0)  # 다리의 트럭 수
        while truck + sum(bridge) > weight or truckOnBridge + 1 > bridge_length or bridge[0] != 0:
            second += 1
            bridge.rotate(1)  # 오른쪽으로 1칸씩 쉬프팅
            bridge.popleft()  # 맨 오른쪽에 있던애가 맨앞으로 왔으니 얜 빼고
            bridge.appendleft(0)  # 걔 대신 0을 넣어준다
            truckOnBridge = bridge_length - bridge.count(0)  # 다리를 빠져나가는 트럭이 있으면 변할수있으니 체크

        bridge.popleft()  # 맨앞칸에 0을 빼고
        bridge.appendleft(truck)  # 맨앞에 트럭을 넣어준다

    second += bridge_length  # 마지막 트럭이 들어가고 for문이 끝나니까 다리 길이만큼 초가 지나야 마지막 트럭이 빠져나감

    return second