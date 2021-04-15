from collections import deque, Counter

def solution(priorities, location):
    answer = 0
    dq = deque(priorities)
    counter = Counter(priorities)
    
    # 요청 문서보다 높은 우선순위의 문서 개수
    num_prior = 0  
    # 요청 문서의 deq에서의 위치(idx) 저장
    current_prior = dq[location]
    
    # 요청 문서보다 높은 우선순위의 문서 개수 저장
    for num in counter:
        if num>current_prior:
            num_prior +=counter[num]
    
    # 요청 문서의 순서
    wait=1

    while(num_prior>0):       
        top = dq.popleft() 
        """ 
        max 쓰면 counter 안써도 됨
        if top < max(dq):
            dq.append(top)
        """ 
        # dq에 현재 문서보다 우선순위 문서가 있으면 뒤로감
        # 없으면 dq에서 제거처리, wait 증가
        for num in counter: 
            if top < num:
                dq.append(top)
                break  
        else:
            counter[top]-=1
            if counter[top]==0: del counter[top]
            wait+=1
            num_prior-=1
        # 요청 문서의 위치 조정 
        location = location-1 if location>0 else len(dq)-1
    
    # 요청 문서가 최상위 우선순위이지만, 동일 우선순위의 문서들 처리
    for i,prior in enumerate(dq):
        if i>=location:
            break
        if prior==current_prior:
            wait+=1
    
    return wait
