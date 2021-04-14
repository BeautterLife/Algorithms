import math
def solution(brown, yellow):
    answer = []
    # 높이 <= 가로 이므로 가로부터
    for height in range(3,int(math.sqrt(yellow+brown))+1):
        if (brown+yellow)%height ==0:
            width=(brown+yellow)//height
            
            if((height-2)*(width-2)) == yellow:
                answer.append(width)
                answer.append(height)
                break
    return answer
