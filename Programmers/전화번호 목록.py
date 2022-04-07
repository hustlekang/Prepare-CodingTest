def solution(phone_book):
    answer = True
    length = len(phone_book)
    phone_book.sort(key=lambda x: len(x))  # 2.순서대로 정렬 한 것중에 길이대로 정렬
    phone_book.sort()  # 1.앞에숫자부터 기준으로 순서대로 정렬

    for i in range(length):
        if i + 1 < length:
            if phone_book[i + 1].startswith(phone_book[i]):
                answer = False
                break

    return answer