import heapq
"""
우선순위큐 - heap : min heap(파이썬 기본)
Complete binary tree

삽입 : O(1)
삭제 : O(log N)

힙 정렬 : heap에 insert할 때 우선순위에 맞게 삽입됨

"""

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville)>1 and scoville[0]<K:
        food_1 = heapq.heappop(scoville)
        food_2 = heapq.heappop(scoville)
        
        heapq.heappush(scoville, food_1+food_2*2)
        answer+=1
    
    return answer if scoville[0]>=K else -1
