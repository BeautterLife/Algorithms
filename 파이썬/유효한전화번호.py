# 입력은 "xxx-xxxx-xxxx" 형식의 길이가 n인 문자열
def solution(phone):
    agency = ('010','011','016','017','018','019')
    
    num = ''
    for i in phone:
        if i.isalnum():
            num+=i
            
    if num[0:3] not in agency:
        return ''
    elif not(len(num)==10 or len(num)==11):
        return ''
    
    return num
