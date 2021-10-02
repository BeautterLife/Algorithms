def solution(numbers):
    numset = set([i for i in range(10)]) - set(numbers)
    return sum(numset)
