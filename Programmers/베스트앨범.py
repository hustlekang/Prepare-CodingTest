def solution(genres, plays):
    answer = []
    playedByGenre = {} #장르별 곡정보 (플레이수,곡번호)
    genreOrder = [] # 장르별 속한 노래 총 재생 횟수

    for i in range(len(genres)):
        if genres[i] in playedByGenre.keys():
            playedByGenre[genres[i]].append((plays[i], i))
        else:
            playedByGenre[genres[i]] = [(plays[i], i)]

    for genre in playedByGenre.keys():
        playedByGenre[genre].sort(key=lambda x: x[1]) # 2. 플레이수 같으면 곡번호 낮은 순
        playedByGenre[genre].sort(key=lambda x: x[0], reverse=True) # 1. 플레이수가 많은 순

    for genre in playedByGenre.keys():
        genreOrder.append((genre, sum(i[0] for i in playedByGenre[genre])))

    genreOrder.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(genreOrder)):
        genre = genreOrder[i][0]
        cnt = 0
        for song in playedByGenre[genre]:
            if cnt == 2: #최다 재생곡 2곡만
                break
            answer.append(song[1])
            cnt += 1

    return answer