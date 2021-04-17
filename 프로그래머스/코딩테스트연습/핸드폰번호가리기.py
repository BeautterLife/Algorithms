def solution(phone_number):
    answer = ['*'*(len(phone_number)-4)]
    answer.append(phone_number[-4:])
    #answer.extend(phone_number[-4:])    문자열이 iterable이라 extend(iterable) 됨
    return ''.join(answer)
  
    #return '*'*(len(phone_number)-4)+phone_number[-4:]
    
    #정규식도 해보기
