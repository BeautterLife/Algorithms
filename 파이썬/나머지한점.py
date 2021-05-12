# 직사각형의 4개 좌표중 3개만 주어졌을 때, 나머지 한 점의 좌표를 구하는 문제

def solution(v):
    answer = []
    
    a,b = zip(*(v))
    
    for dot in a:
        if a.count(dot)==1:
            answer.append(dot)
            break
    for dot in b:
        if b.count(dot)==1:
            answer.append(dot)
            break
    return answer
