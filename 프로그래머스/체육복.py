def solution(n, lost, reserve):
    answer = 0
    reserve_set = set(reserve) - set(lost)
    lost = list(set(lost) - set(reserve))
    
    for i in sorted(lost):
        if i-1 in reserve_set:
            answer+=1
            reserve_set.remove(i-1)
        elif i+1 in reserve_set:
            reserve_set.remove(i+1)
            answer+=1
        elif not reserve_set:
            break
            
    return answer + n - len(lost)
