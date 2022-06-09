def solution(arr):
    answer= [0,0]
    def zip(graph):
        n = len(graph)
        if n == 1:
            if graph[0][0]==0: # 4등분 할 때 하나가 되어도 [0],[1] 형태가 아닌 [[0]],[[1]] 형태임
                answer[0]+=1
            else:
                answer[1]+=1
            return

        firstblock = graph[0][0]
        possible = True
        for line in graph:
            for block in line:
                if block != firstblock:
                    possible = False
                    break

        if possible:
            if firstblock==0:
                answer[0]+=1
            else:
                answer[1]+=1
            return
        # 4등분 할 때 하나가 되어도 [0],[1] 형태가 아닌 [[0]],[[1]] 형태임
        section_2 = [i[:int(n / 2)] for i in graph[:int(n/2)]]
        section_1 = [i[int(n / 2):] for i in graph[:int(n/2)]]
        section_3 = [i[:int(n / 2)] for i in graph[int(n/2):]]
        section_4 = [i[int(n / 2):] for i in graph[int(n/2):]]

        zip(section_1)
        zip(section_2)
        zip(section_3)
        zip(section_4)

    zip(arr)
    return answer


print(solution([[1,1],[0,0]]))