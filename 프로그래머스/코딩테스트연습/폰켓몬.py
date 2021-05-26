def solution(nums):
    pmon = set(nums)
    if len(pmon)>= len(nums)//2:
        return len(nums)//2
    return len(pmon)
