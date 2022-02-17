n=5 # 데이터의 개수
m=5 # 목표 부분합
data=[1,2,3,2,5] #데이터의 리스트
count=0 #부분합이 m인 수열의 개수 초기화
interval_sum=0 #수열의 부분합 초기화
end=0 #끝점을 0으로 설정 후 시작

for start in range(n): #시작점은 0부터 증가시킴
    while interval_sum<m and end<n: #부분합이 m보다 작으면 계속 end를 증가시킴, end<n 은 정상범위조건
        interval_sum += data[end] # 목표 부분합보다 커질때까지 계속 증가시킴
        end+=1
    if interval_sum==m: # 부분합>=m 일때 while문 탈출하고,부분합=m이면 count해준다
        count+=1

    interval_sum -= data[start] #부분합이 m보다 크다면 start값을 빼주고 다음 for문으로 이동하면 start를 한칸 오른쪽으로 이동한 꼴
print(count)
