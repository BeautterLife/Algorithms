def solution(numbers):
    answer = set()
    for i,num1 in enumerate(numbers[:-1]):
        for num2 in numbers[i+1:]:
            answer.add(num1+num2)
    #sorted(list)  vs  list.sort()
    #list.sort()는 안됨 : 정렬된 결과를 반환하지 않음(반환값이 없음)
    #answer.sort() 후 return answer
    return sorted(list(answer))
