def solution(s):
    answer = []
    str = s[2:-2].replace("},","")
    set_list = []
    for a in str.split("{"):
        temp=set()
        for x in a.split(","):
            temp.add(int(x))
        set_list.append(temp)
    
    sorted_set_list = sorted(set_list, key = lambda x : len(x))
    for subset in sorted_set_list:
        for c in subset:
            if c not in answer:
                answer.append(c)
                break
                
    return answer
