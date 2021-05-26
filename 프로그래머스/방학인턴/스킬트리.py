def solution(skill, skill_trees):
    answer = 0
    
    for skillset in skill_trees:
        j = 0
        for s in skillset:
            # skill에 있는데 해당 순서에 안배우면 실패
            if s in skill[j:]:
                if not skill[j]==s:
                    break
                j+=1
        # 꼭 skill에 있는것을 다 배울 필요 없음, skill의 순서를 위배하지 않으면 됨
        # skill에 있는 것을 아무것도 안배워도 성공
        else:
            answer+=1

def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        idx=0
        isOk=True
        for i in sk:
            inIndex =  skill.find(i)
            if inIndex > idx:
                isOk=False
                break
            if inIndex == idx:
                idx+=1
        if isOk:
            answer+=1
    
    
        
            
    return answer
