def solution(n, words):
    answer = []
    word_set={words[0]} # set(words[0]) -> iterable 객체에서 element를 만들어줌 (X)
    
    for i,word in zip(range(1,len(words)),words[1:]):
        if word in word_set or words[i][0]!=words[i-1][-1]:
            answer.append(i%n+1)
            answer.append((i+1)//n if (i+1)%n==0 else (i+1)//n+1)  # 문제 번호(실제 번호, 인덱스X)는 i+1
            break
        word_set.add(word)
        
    # for-else : 끝말잇기 정상종료
    else:
        answer.append(0)
        answer.append(0)
    return answer
