def solution(s):
    answer = ''
    num_dic = {'zero':'0','one':'1','two':'2','three':'3', 'four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    start=0
    for i,ch in enumerate(s): 
        if ch.isdigit():
            answer +=ch
            start = i+1
        else:
            if s[start:i+1] in num_dic:
                answer += num_dic[s[start:i+1]]
                start = i+1
            
    return int(answer)
