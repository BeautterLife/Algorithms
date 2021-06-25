import math

def solution(n, arr1, arr2):
    answer = []
    
    for line1, line2 in zip(arr1, arr2):
        ans = line1 | line2
        string=''
        
        # n자리의 string을 만들어야하므로 기준을 만듦.
        # ans로만 하면 2^(n-1)-1이하의 ans들은 왼쪽 공백을 채울 수 없음
        std = pow(2,n)-1
        
        while std >=1:
            string+='#' if ans%2==1 else ' '
            ans//=2
            std//=2
          
        # 만든 string의 역순
        answer.append(string[::-1])
    return answer
