def solution(arr):
    answer=[arr[0]]
    for num in arr[1:]:
        if num!=answer[-1]:
            answer.append(num)
    return answer
  
  # 중복 숫자 제거+입력순서 유지
  # python 3.x 이상부터는 dictionary가 입력순서를 기억함.
  # from collections OrderedDict도 있음
