def solution(s):
    answer = 0
    
    p1 = ['(',')']
    p2 = ['{','}']
    p3 = ['[',']']
    s = s[-1]+s[0:-1]

    for i in range(len(s)):
        s = s[1:]+s[0]
        stack = []
        for p in s:
            stack.append(p)
            if len(stack)>=2:
                if stack[-2:]== p1 or stack[-2:] == p2 or stack[-2:] == p3:
                    stack.pop()
                    stack.pop()
            
        if len(stack)==0:
            answer+=1
    
    return answer
