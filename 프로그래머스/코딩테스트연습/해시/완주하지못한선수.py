from collections import Counter

def solution(participant, completion):
    participant_dict = Counter(participant)
    completion_dict = Counter(completion)
    
    for person in participant_dict:
        if participant_dict[person]!=completion_dict[person]:
            return person
    return ''
    """
    a = (participant_dict-completion_dict).items()  -> dict_items() iterator 반환
    for p,_ in a:
        return p
    """
