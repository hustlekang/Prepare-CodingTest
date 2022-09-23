# 문자열에서 a가 총 6개면
# aaaaaa로 만들어야하니 길이가 6인 구간에서 b가 가장 적은 곳에다가 그 갯수만큼 이동하면 최소값
# ex) abbaaa : b 2개를 a로 바꿔야하니 cnt=2, aaaaba : b 1개만 바꾸면 되니 cnt=1
def solution(string):
    n = string.count('a')
    cnt = n
    length = len(string)
    string += string # 뒤에도 연결된것이니 걍 string 붙침
    for i in range(length):
        cnt = min(cnt, string[i:(i+n)].count('b'))

    return cnt

if __name__ == '__main__':
    string = input().strip()
    answer = solution(string)
    print(answer)