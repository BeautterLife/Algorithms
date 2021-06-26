# dictionary 이용한 풀이
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        # 스킬트리의 위치를 저장하는 dictionary
        # skill에 없으면 -1, 있으면 skill에서의 idx를 저장
        skill_dic = {sk:skill.find(sk) for sk in skill_tree}
        #스킬을 배울 순서
        skill_idx = 0

        # skill_tree의 스킬 하나씩 검사
        for sk in skill_tree:
            # skill에 있는 스킬이면
            if skill_dic[sk]>=0:
                # 해당 순서가 아니면 못배움
                if skill_dic[sk] != skill_idx:
                    print(sk, 'd')
                    break
                # 스킬 배울 순서를 하나 증가
                skill_idx+=1
        
        # skill_tree의 모든 스킬을 skill 순서를 지켜서 배웠다면 정답
        else:
            answer+=1
    return answer

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
