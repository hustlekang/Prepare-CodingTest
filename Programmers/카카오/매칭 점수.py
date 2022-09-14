import re

# html 형식의 문자열에서 url을 찾는 함수
def findUrl(html):
    reg = re.compile('<meta property="og:url" content="https://[a-zA-Z0-9\./]+"/>')
    metaTag = reg.search(html).group()
    url = metaTag.split('https://')[1][:-3]
    return url

# html 형식에서 a태그로 연결한 url들을 배열에 담아 반환하는 함수
def findLink(html):
    reg = re.compile('<a href="https://[a-zA-z0-9\./]+">')
    aTagList = reg.findall(html)
    linkList = list(map(lambda x:x.split('https://')[1][:-2],aTagList))
    return linkList

# 기본 점수를 계산하는 함수
def caculateBaseScore(html,word):
    # score = len(re.findall('[^a-zA-Z]{}'.format(word), html, re.I)) # 8muzimuzi를 맞다고 하는 오류
    # score = len(re.findall('[^a-zA-Z]{}[^a-zA-Z]'.format(word), html, re.I))  # 8muzi8muzi! 를 2개인데 1개로 보는 오류
    score = list(map(str.lower, re.findall('[a-zA-Z]+',html))).count(word.lower())
    return score

def solution(word, pages):
    answer = [-1,-1] # [매칭점수, 페이지 번호]
    scoreBoard = {}
    linkBoard = {} # url1 : [url2...] url1로 링크가 걸린 다른 페이지들

    # scoreBoard의 key 값으로 모든 페이지의 url = {} 로 초기화
    for page in pages:
        url = findUrl(page)
        scoreBoard[url] = {'base' : 0, 'outLink' : 0, 'link' : 0}
        linkBoard[url] = []

    # 외부 링크수 구하기
    for page in pages:
        url = findUrl(page)
        linkList = findLink(page)
        scoreBoard[url]['outLink'] += len(linkList) # 외부링크수 계산
        scoreBoard[url]['base'] = caculateBaseScore(page,word) # 기본점수 계산

        for link in linkList: # 다른곳으로 이어진 얘 추가
            if link not in linkBoard.keys(): # a태그로 이동하는 페이지가 pages 배열에 없을 수도 있음
                continue
            linkBoard[link].append(url)

    # 링크점수 구하고 매칭점수 구하기
    for idx, page in enumerate(pages):
        url = findUrl(page)
        for connectedUrl in linkBoard[url]: # 링크점수 계산
             scoreBoard[url]['link'] += scoreBoard[connectedUrl]['base']/scoreBoard[connectedUrl]['outLink']

        matchingScore = scoreBoard[url]['base'] + scoreBoard[url]['link']

        if answer[0] < matchingScore:
            answer = [matchingScore, idx]
        elif answer[0] == matchingScore and answer[1] > idx:
            answer[1] = idx

    return answer[1]