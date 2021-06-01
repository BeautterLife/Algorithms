from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    # mutated during iteration 확인하기!
    
    while(progresses):
        answer.append(0)
        isCompleted = False
        # int 형변환은 math.trunc() - 내림효과(정수부만 취함)
        day = math.ceil((100-progresses[0])/speeds[0])
        # 현재 dq와 이웃하고, 완료된 것들까지.
        pop_idx = 0 
        for i in range(len(progresses)):
            progresses[i]+=day*speeds[i]
            
            if (not isCompleted) and progresses[i]>=100: 
                answer[-1]+=1
                pop_idx = i
                
            else:
                isCompleted = True

        for i in range(pop_idx+1):
            progresses.popleft()
            speeds.popleft()
            
    return answer
