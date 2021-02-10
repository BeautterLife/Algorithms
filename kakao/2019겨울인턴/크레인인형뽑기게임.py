def solution(board, moves):
    answer = 0
    stack = []
    arrLen = len(board)
    for move in moves:
        for i in range(arrLen):
            if board[i][move-1] !=0:
                stack.append(board[i][move-1])
                board[i][move-1]=0
                break
        
        if len(stack)>1 and stack[-1]==stack[-2]:
            answer+=2
            stack.pop()
            stack.pop()
        
    return answer
