def solution(board, moves):
    answer = 0
    result = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if result and result[-1] == board[j][i-1]:
                    result.pop()
                    answer += 2
                else:
                    result.append(board[j][i-1])
                
                board[j][i-1] = 0

                break
            
    return answer