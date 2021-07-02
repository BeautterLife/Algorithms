def solution(record):
    answer = []    
    id_nic = dict()
    msg = {'enter': '님이 들어왔습니다.', 'leave': '님이 나갔습니다.'}
    
    # 3가지 state에 따라서 리스트에 state와 uid 저장
    # uid(info[1])와 nic name을 사전에 저장하고, 변경되면 업데이트
    for rc in record:
        info = rc.split()
        if info[0] == 'Enter':
            id_nic[info[1]] = info[2]
            answer.append([info[1],'enter'])
        elif info[0] == 'Change':
            id_nic[info[1]] = info[2]
        else:
            answer.append([info[1],'leave'])
    
    # 실제 채팅방 구성
    # 최종 id-nic name 매칭
    for i, lst in enumerate(answer):
        answer[i] = id_nic[lst[0]] + msg[lst[1]]
        
    return answer
