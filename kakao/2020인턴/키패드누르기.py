def solution(numbers, hand):
    answer = []

    left = (1,4,7)
    right = (3,6,9)
    
    w1 = {2:1,5:2,8:3,0:4}
    w4 = {2:2,5:1,8:2,0:3}
    w7 = {2:3,5:2,8:1,0:2}
    w_star = {2:4, 5:3, 8:2, 0:1}
    
    w2 = {2:0,5:1,8:2,0:3}
    w5 = {2:1,5:0,8:1,0:2}
    w8 = {2:2,5:1,8:0,0:1}
    w0 = {2:3,5:2,8:1,0:0}
    
    w3 = {2:1,5:2,8:3,0:4}
    w6 = {2:2,5:1,8:2,0:3}
    w9 = {2:3,5:2,8:1,0:2}
    w_sharp = {2:4, 5:3, 8:2, 0:1}
    
    weight_dict = {1:w1, 4:w4, 7: w7, 3:w3, 6:w6, 9:w9, 2:w2, 5:w5, 8:w8, 0:w0,'*':w_star, '#':w_sharp}
    
    position_l = '*'
    position_r = '#'

    for i in numbers:
        if i in left:
            position_l = i
            answer.append('L')
        elif i in right:
            position_r = i
            answer.append('R')
        else:
            if weight_dict[position_l][i] < weight_dict[position_r][i]:
                position_l = i
                answer.append('L')
            elif weight_dict[position_l][i] > weight_dict[position_r][i]:
                position_r = i
                answer.append('R')
            else:
                if hand=="left":
                    position_l = i
                    answer.append('L')
                else:
                    position_r = i
                    answer.append('R')

    return ''.join(answer)
