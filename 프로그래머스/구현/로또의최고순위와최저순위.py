def solution(lottos, win_nums):
    answer = []
    num_zero = 0
    set_win_nums = set(win_nums)
    low_rank = 6
    correct_num=0
    
    for lotto in lottos:
        if lotto == 0:
            num_zero+=1
        else:
            if lotto in set_win_nums:
                correct_num +=1    
    # 최고 등수는 0 개수와 맞은 개수를 빼고 이 합이 1을 넘으면 1을 더해준다(5등은 2개맞아야 되므로)
    high_rank = low_rank - num_zero - correct_num + (1 if num_zero+correct_num>1 else 0)
    # 최저 등수는 맞은 개수를 빼는데, 맞은개수가 2 이상이면 1을 빼준다
    return [high_rank, low_rank-(correct_num-1 if correct_num>1 else 0)]
