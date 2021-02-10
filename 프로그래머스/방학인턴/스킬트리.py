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
