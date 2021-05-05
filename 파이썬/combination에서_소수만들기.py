# from itertools import combinations
# combinations(iterator, num_elements)

import math

def availablePrimeNum(comb):
    num = sum(comb)
    for i in range(2,int(math.sqrt(sum(comb)))+1):
        if num%i==0:
            return 0
    return 1

# 조합 순서쌍 튜플을 반환하는 제네레이터
def combinations(nums):
    for i,num1 in enumerate(nums):
        for j,num2 in enumerate(nums[i+1:]):
            k = i+j+1
            for num3 in nums[k+1:]:
                yield (num1,num2,num3)
    """            
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                yield (nums[i]+nums[j]+nums[k])
    """

def solution(nums):
    answer = 0
    
    for i in combinations(nums):
        answer+=availablePrimeNum(i)

    return answer
