def solution(phone_book):
    phone_book.sort()
    for i,word in enumerate(phone_book[1:]):
        if phone_book[i] == word[:len(phone_book[i])]:
            return False
    return True
