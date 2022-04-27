# 처음에 모든 키들의 값을 순회하면서 1이상 인지 확인을 해서 시간 초과
# (키값의 종류 개수 = 전체 상품의 종류)로 체크 하면 됨
def solution(gems):
    shortest =100000 # 가장 짧은 거리 초기화
    answer =()
    cart ={} # {키=상품명 : 값=개수}
    types =len(set(gems)) # 모든 상품의 개수

    end =0
    for start in range(len(gems)):
        while len(cart)!=types and end <len(gems):
            if gems[end] in cart.keys(): # 이미 있는 상품이면 갯수 +1
                cart[gems[end]]+=1
            else:
                cart[gems[end]]=1 # 없는 상품이면 1
            end+=1 # end값 올려서 만족할때까지 반복

        # while 문을 end가 마지막까지 가서 탈출한 것이면  len(cart) == types 를 만족 안하기 때문에 한번더 체크
        if len(cart)==types and end-start <shortest: # 상품 종류=모든 상품의 개수 and 만족하는 길이의 최소값보다 작을 때
            answer = (start,end-1,end-start)
            shortest = end-start # 가장 짧은 방법 초기화

        cart[gems[start]]-=1 # start부분에서 담은 상품은 빼준다
        if cart[gems[start]]==0: # 갯수가 0이면 아예 삭제해서 len(cart)==types 조건으로 탐색이 가능하게 유지
            del cart[gems[start]]

    return [answer[0]+1 ,answer[1]+1]