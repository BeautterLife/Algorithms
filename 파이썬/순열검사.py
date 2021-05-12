def solution(arr):
    
    if len(arr)!=max(arr):
        return False
    
    s = set()
    
    for num in arr:
        if num in s:
            return False
        s.add(num)

    return True
