def solution(absolutes, signs):
    answer = 0
    for num,sign in zip(absolutes,signs):
        answer+=num * (1 if sign else -1)
    return answer
