from collections import deque
def solution(n, edge):
    #a,b = list(zip(*edge)) -> 차원별 언패킹
    #edge*=2  얕은 복사
    #edge.extend([row[::-1] for row in edge if row[0]!=1]) 양방향 간선 추가 시도
    
    graph = {i:set() for i in range(1,n+1)} # node i 와 연결된 node 추가하기위해 {node번호:empty set}을 원소로 갖는 dictionary
    # 양방향 간선 추가
    # dict[key] key가 없는 경우 key error 리턴.
    for a,b in edge:
        graph[a].add(b)
        graph[b].add(a)

    #node_set = set([row[0] for row in edge])  
    #graph = {i:set(row[1] for row in edge if row[0]==i) for i in range(1,n+1)} -> 연결리스트(정확히는 set)로 그래프 만들지만 O(n^2)라서 시간 초과

    visit = {i:20000 for i in range(2,n+1)}  # 각 node로의 최단 거리, 초기에는 총 노드수 20000으로 초기화(노드 거리는 전체 노드-1 이 최대)
    visit[1]=0   # source 1은 최단거리 0
    dq = deque([1])  # deque에 source 추가

    
    while(dq):
        top = dq.popleft
        # 개념적으로) 인접리스트를 순회하여 이전 최단거리보다 짧은 거리 발견시 최단거리 재할당 및 queue에 추가
        for next in graph[top]:
            if visit[next] <= visit[top] +1:
                continue
                          
            visit[next] = visit[top]+1 
            dq.append(next)
           
    # dict.values() : dict.values 타입의 iterable 객체 반환.
    # list로 형변환하여 가장긴 최단거리를 갖는 노드 개수 count
    # dict.values는 count 함수가 없고
    # tuple, list는 있음.  -> count() 조사하기
    return list(visit.values()).count(max(visit.values()))
