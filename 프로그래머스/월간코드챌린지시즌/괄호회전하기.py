def solution(s):
    answer = 0
    
    p1 = ['(',')']
    p2 = ['{','}']
    p3 = ['[',']']
    not_p = [')','}',']']
    s = s[-1]+s[0:-1]

    for i in range(len(s)):
        s = s[1:]+s[0]
        
        stack = []
        for p in s:
            stack.append(p)
            # append했을때 짝지은 괄호가 아니면 올바른 괄호가 아님.
            if len(stack)>=2:
                if stack[-2:]== p1 or stack[-2:] == p2 or stack[-2:] == p3:
                    stack.pop()
                    stack.pop()
                    
                elif p in not_p:
                    break
        if len(stack)==0:
            answer+=1
    
    return answer
