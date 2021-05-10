def solution(answers):
    #answer = []
    pick = {
        1:[1, 2, 3, 4, 5],
        2:[2, 1, 2, 3, 2, 4, 2, 5],
        3:[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    
    cnt_1,cnt_2,cnt_3=0,0,0
    
    for i,answer in enumerate(answers):
        if pick[1][i%5] == answer:
            cnt_1+=1
        if pick[2][i%8] == answer:
            cnt_2+=1
        if pick[3][i%10] == answer:
            cnt_3+=1
    
    answer=[[1,cnt_1],[2,cnt_2],[3,cnt_3]]
    answer = sorted(answer, key=lambda x : x[1])
    
    if answer[2][1]==answer[1][1]:
        if answer[2][1]!= answer[0][1]:
            del answer[0]
    else:
        #print(answer[:2][:])
        del answer[:2]
    print(answer[0])
    #answer2 = answer[:][1]    -> column 추출은 이 방식으로 안됨
    #                          -> 리스트를 뒤집어서 1행 추출하거나 unzip
    #                            new_list = list(map(list, zip(*mylist)))
    
    return sorted(list(zip(*answer))[0])

"""
def solution(answers):
    answer = []
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    s_answer=[0,0,0]

    len_s1 = 5
    len_s2 = 8
    len_s3 = 10

    for i,answer in enumerate(answers):
        if student_1[i%len_s1] == answer:
            s_answer[0]+=1
        if student_2[i%len_s2] == answer:
            s_answer[1]+=1
        if student_3[i%len_s2] == answer:
            s_answer[2]+=1

    max_answer = max(s_answer)
    #print(max_answer)

    return [i+1 for i,s_num in enumerate(s_answer) if s_num==max_answer]
"""
