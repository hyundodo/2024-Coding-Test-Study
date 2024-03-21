def solution(board, moves):
    stack = [[] for _ in range(len(board))]
    for l in board:
        for idx, e in enumerate(l): # 역순으로 넣어야 함
            if e != 0:
                stack[idx].append(e)
    
    stack_result = []
    answer = 0
    for m in moves:
        pick = stack[m-1].pop()
        if stack_result and stack_result[-1] == pick:
            answer += 2
        else:
            stack_result.append(pick)
    
    return answer

if __name__ == "__main__":
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    print(solution(board, moves)) # 4