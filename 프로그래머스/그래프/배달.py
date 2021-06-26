import heapq

def solution(N, road, K):
    
    #deliver_time = [500001 for _ in range(N)]
    
    # 양방향 그래프 : node간 vertex(배달시간) 저장
    # dictionary로 구현하면 더 빠를 것.
    graph = [[] for _ in range(N+1)]
    deliver_time = [500001]*(N+1)
      
    for info in road:
        graph[info[0]].append([info[1],info[2]])
        graph[info[1]].append([info[0],info[2]])
    
    dijkstra(deliver_time, graph)
    
    answer = [i for i,time in enumerate(deliver_time) if time <= K]
    #print(answer)
    return len(answer)

def dijkstra(deliver_time, graph, start=1):
    q = []
    
    # 우선순위큐(min heap) : 시작 노드로부터 최단 배달시간을 구하여 저장
    # 최단 배달시간을 구한 노드와 인접 노드의 최단 배달시간을 구하는 것을 반복
    heapq.heappush(q,(0, start))
    deliver_time[start] = 0
    
    while q:
        time, node = heapq.heappop(q)
        #print(node,deliver_time, end='')
        
        if deliver_time[node] >= time:
            # 현재 노드와 인접한 노드로 부터 인접 노드로의 최단 배달시간을 계산하여
            # 기존 값에서 갱신되면 heappush
            for i in graph[node]:
                d_time = time+i[1]
                if d_time < deliver_time[i[0]]:
                    deliver_time[i[0]] = d_time
                    heapq.heappush(q, (d_time, i[0]))
        #print(deliver_time)
